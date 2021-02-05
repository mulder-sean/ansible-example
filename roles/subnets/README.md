### Create
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=subnets variables_file=test-data/create.yml independent_test='true'"  
```  

### Destroy
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=subnets variables_file=test-data/destroy.yml  independent_test='true'"  
```  

### Output
Registers a global variable: __created_subnet_info__ with output:
```python
{
  'results': [{
    'changed': True,
    'subnet': {
      'availability_zone': 'us-east-1a',
      'availability_zone_id': 'use1-az2',
      'available_ip_address_count': 1019,
      'cidr_block': '10.20.4.0/22',
      'default_for_az': False,
      'map_public_ip_on_launch': True,
      'map_customer_owned_ip_on_launch': False,
      'state': 'available',
      'vpc_id': 'vpc-0adcd5ea40b2f5f89',
      'owner_id': '111111111111',
      'assign_ipv6_address_on_creation': False,
      'ipv6_cidr_block_association_set': [],
      'tags': {
        'Name': 'ansible_a_public'
      },
      'subnet_arn': 'arn:aws:ec2:us-east-1:111111111111:subnet/subnet-04c343400c292c0e2',
      'id': 'subnet-04c343400c292c0e2',
      'ipv6_cidr_block': '',
      'ipv6_association_id': ''
    },
    'invocation': {
      'module_args': {
        'profile': 'default',
        'az': 'us-east-1a',
        'cidr': '10.20.4.0/22',
        'map_public': True,
        'state': 'present',
        'tags': {
          'Name': 'ansible_a_public'
        },
        'vpc_id': 'vpc-0adcd5ea40b2f5f89',
        'debug_botocore_endpoint_logs': False,
        'validate_certs': True,
        'ipv6_cidr': '',
        'assign_instances_ipv6': False,
        'wait': True,
        'wait_timeout': 300,
        'purge_tags': True,
        'ec2_url': None,
        'aws_secret_key': None,
        'aws_access_key': None,
        'security_token': None,
        'region': None
      }
    },
    'failed': False,
    'subs': {
      'az': 'us-east-1a',
      'cidr_block': '10.20.4.0/22',
      'map_public': 'yes',
      'Name': 'ansible_a_public'
    },
    'ansible_loop_var': 'subs'
  }, {
    'changed': True,
    'subnet': {
      'availability_zone': 'us-east-1a',
      'availability_zone_id': 'use1-az2',
      'available_ip_address_count': 1019,
      'cidr_block': '10.20.16.0/22',
      'default_for_az': False,
      'map_public_ip_on_launch': False,
      'map_customer_owned_ip_on_launch': False,
      'state': 'available',
      'vpc_id': 'vpc-0adcd5ea40b2f5f89',
      'owner_id': '111111111111',
      'assign_ipv6_address_on_creation': False,
      'ipv6_cidr_block_association_set': [],
      'tags': {
        'Name': 'ansible_a_private'
      },
      'subnet_arn': 'arn:aws:ec2:us-east-1:111111111111:subnet/subnet-049de2d67e21a5ec0',
      'id': 'subnet-049de2d67e21a5ec0',
      'ipv6_cidr_block': '',
      'ipv6_association_id': ''
    },
    'invocation': {
      'module_args': {
        'profile': 'default',
        'az': 'us-east-1a',
        'cidr': '10.20.16.0/22',
        'map_public': False,
        'state': 'present',
        'tags': {
          'Name': 'ansible_a_private'
        },
        'vpc_id': 'vpc-0adcd5ea40b2f5f89',
        'debug_botocore_endpoint_logs': False,
        'validate_certs': True,
        'ipv6_cidr': '',
        'assign_instances_ipv6': False,
        'wait': True,
        'wait_timeout': 300,
        'purge_tags': True,
        'ec2_url': None,
        'aws_secret_key': None,
        'aws_access_key': None,
        'security_token': None,
        'region': None
      }
    },
    'failed': False,
    'subs': {
      'az': 'us-east-1a',
      'cidr_block': '10.20.16.0/22',
      'map_public': 'no',
      'Name': 'ansible_a_private'
    },
    'ansible_loop_var': 'subs'
  }],
  'changed': True,
  'msg': 'All items completed'
}
```
