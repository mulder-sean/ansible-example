#!/usr/bin/python

from ansible.module_utils.basic import *

DOCUMENTATION = '''
---
module: BUILD_NAT_SUBNET_MAPPING
short_description: Build map of private subnets to nat gateways
author: "Sean Mulder"
notes:
'''

EXAMPLES = '''
- BUILD_NAT_SUBNET_MAPPING:
    subnet_info=[]
    nat_gateway_info=[]
'''


def main():
    module = AnsibleModule(
        argument_spec=dict(
            subnet_info=dict(required=True, type='list'),
            nat_gateway_info=dict(required=True, type='list')
        )
    )

    p = module.params
    subnet_info = p['subnet_info']
    nat_gateway_info = p['nat_gateway_info']

    # Create object which will be returned
    mapped_results = []

    # Create dict for mapping out data
    zones = {}

    # Process logic only if both inputs have data otherwise skip
    if subnet_info and nat_gateway_info:

        # Loop through subnet data only once
        for si in subnet_info:

            # Create easy to understand reference
            subnet_public = si.get('subnet').get('map_public_ip_on_launch')
            subnet_zone = si.get('subnet').get('availability_zone')
            subnet_id = si.get('subnet').get('id')

            # Create zone in dict for first entry
            if not zones.get(subnet_zone):
                zones[subnet_zone] = {}

            # Fetch zone from dict
            current_zone = zones.get(subnet_zone)

            # Process public subnets
            if subnet_public:

                # Create public in dict for first entry
                if not current_zone.get('public'):
                    current_zone['public'] = {}

                # Fetch public from dict
                current_public = current_zone.get('public')

                # Create list of subnet ids for first entry
                if not current_public.get('subnet_ids'):
                    current_public['subnet_ids'] = []

                # Fetch subnet ids from dict
                current_public_ids = current_public.get('subnet_ids')

                # Update list with current subnet_id
                current_public_ids.append(subnet_id)

                # Loop through all nat gateways
                for ngi in nat_gateway_info:

                    # If nat subnet matches current subnet
                    if ngi.get('subnet_id') == subnet_id:

                        # add it to the zone for reference by private subnets
                        current_zone['nat_gateway_id'] = ngi.get('nat_gateway_id')

            # Process private subnets
            else:

                # Create private in dict for first entry
                if not current_zone.get('private'):
                    current_zone['private'] = {}

                # Fetch private from dict
                current_private = current_zone.get('private')

                # Create list of subnet ids from dict for first entry
                if not current_private.get('subnet_ids'):
                    current_private['subnet_ids'] = []

                # Fetch list of subnet ids from dict
                current_private_ids = current_private.get('subnet_ids')

                # Update list with current subnet id
                current_private_ids.append(subnet_id)

        # Loop through fully built dict
        for zone, data in zones.items():

            # Convert dict into list for ease of access with ansible loop
            mapped_results.append({
                'zone': zone,
                'public_subnets': data.get('public').get('subnet_ids'),
                'private_subnets': data.get('private').get('subnet_ids'),
                'nat_gateway_id': data.get('nat_gateway_id')
            })

    module.exit_json(changed=True, results=mapped_results)


if __name__ == '__main__':
    main()
