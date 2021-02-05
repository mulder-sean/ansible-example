### Create
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=ec2 variables_file=test-data/create.yml independent_test='true'"  
```  

### Destroy
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=ec2 variables_file=test-data/destroy.yml  independent_test='true'"  
```  

### Output
Registers a global variable: __private_security_group_info__ with output:
```python
{
  'security_groups': [{
    'description': 'ansible-private',
    'group_name': 'ansible-private',
    'ip_permissions': [{
      'from_port': 8080,
      'ip_protocol': 'tcp',
      'ip_ranges': [],
      'ipv6_ranges': [],
      'prefix_list_ids': [],
      'to_port': 8080,
      'user_id_group_pairs': [{
        'group_id': 'sg-0db01c4c84a4d759a',
        'user_id': '111111111111'
      }]
    }],
    'owner_id': '111111111111',
    'group_id': 'sg-0ba5922ba122563fc',
    'ip_permissions_egress': [{
      'ip_protocol': '-1',
      'ip_ranges': [{
        'cidr_ip': '0.0.0.0/0'
      }],
      'ipv6_ranges': [],
      'prefix_list_ids': [],
      'user_id_group_pairs': []
    }],
    'tags': {
      'Name': 'ansible-private'
    },
    'vpc_id': 'vpc-0adcd5ea40b2f5f89'
  }],
  'failed': False,
  'changed': False
}
```

Registers a global variable: __created_ec2_instance_info__ with output:
```python
{
  'changed': True,
  'instances': [{
    'ami_launch_index': 0,
    'image_id': 'ami-047a51fa27710816e',
    'instance_id': 'i-05faa9c4b4161dc44',
    'instance_type': 't3.small',
    'launch_time': '2021-02-04T00:09:32+00:00',
    'monitoring': {
      'state': 'disabled'
    },
    'placement': {
      'availability_zone': 'us-east-1a',
      'group_name': '',
      'tenancy': 'default'
    },
    'private_dns_name': 'ip-10-20-19-1.ec2.internal',
    'private_ip_address': '10.20.19.1',
    'product_codes': [],
    'public_dns_name': '',
    'state': {
      'code': 16,
      'name': 'running'
    },
    'state_transition_reason': '',
    'subnet_id': 'subnet-049de2d67e21a5ec0',
    'vpc_id': 'vpc-0adcd5ea40b2f5f89',
    'architecture': 'x86_64',
    'block_device_mappings': [{
      'device_name': '/dev/xvda',
      'ebs': {
        'attach_time': '2021-02-04T00:09:33+00:00',
        'delete_on_termination': True,
        'status': 'attached',
        'volume_id': 'vol-0aa1c348be77323c9'
      }
    }],
    'client_token': '11111111111111111111111111111111',
    'ebs_optimized': False,
    'ena_support': True,
    'hypervisor': 'xen',
    'iam_instance_profile': {
      'arn': 'arn:aws:iam::111111111111:instance-profile/ansible-session-manager',
      'id': '111111111111111111111'
    },
    'network_interfaces': [{
      'attachment': {
        'attach_time': '2021-02-04T00:09:32+00:00',
        'attachment_id': 'eni-attach-0173586ea80ff0bc4',
        'delete_on_termination': True,
        'device_index': 0,
        'status': 'attached',
        'network_card_index': 0
      },
      'description': '',
      'groups': [{
        'group_name': 'ansible-private',
        'group_id': 'sg-0ba5922ba122563fc'
      }],
      'ipv6_addresses': [],
      'mac_address': '12:3b:c7:ee:cc:b5',
      'network_interface_id': 'eni-05bd80b2a6206fb49',
      'owner_id': '111111111111',
      'private_dns_name': 'ip-10-20-19-1.ec2.internal',
      'private_ip_address': '10.20.19.1',
      'private_ip_addresses': [{
        'primary': True,
        'private_dns_name': 'ip-10-20-19-1.ec2.internal',
        'private_ip_address': '10.20.19.1'
      }],
      'source_dest_check': True,
      'status': 'in-use',
      'subnet_id': 'subnet-049de2d67e21a5ec0',
      'vpc_id': 'vpc-0adcd5ea40b2f5f89',
      'interface_type': 'interface'
    }],
    'root_device_name': '/dev/xvda',
    'root_device_type': 'ebs',
    'security_groups': [{
      'group_name': 'ansible-private',
      'group_id': 'sg-0ba5922ba122563fc'
    }],
    'source_dest_check': True,
    'tags': {
      'Name': 'ansible-ec2-test'
    },
    'virtualization_type': 'hvm',
    'cpu_options': {
      'core_count': 1,
      'threads_per_core': 2
    },
    'capacity_reservation_specification': {
      'capacity_reservation_preference': 'open'
    },
    'hibernation_options': {
      'configured': False
    },
    'metadata_options': {
      'state': 'applied',
      'http_tokens': 'optional',
      'http_put_response_hop_limit': 1,
      'http_endpoint': 'enabled'
    },
    'enclave_options': {
      'enabled': False
    }
  }],
  'instance_ids': ['i-05faa9c4b4161dc44'],
  'spec': {
    'ClientToken': '11111111111111111111111111111111',
    'MaxCount': 1,
    'MinCount': 1,
    'NetworkInterfaces': [{
      'DeviceIndex': 0,
      'SubnetId': 'subnet-049de2d67e21a5ec0',
      'Groups': ['sg-0ba5922ba122563fc']
    }],
    'BlockDeviceMappings': [],
    'ImageId': 'ami-047a51fa27710816e',
    'UserData': '#!/bin/bash\\nyum update\\nyum -y install java-1.8.0-openjdk tomcat\\nsystemctl enable amazon-ssm-agent\\nsystemctl start amazon-ssm-agent\\nsystemctl enable tomcat\\nsystemctl start tomcat\\n',
    'EbsOptimized': False,
    'TagSpecifications': [{
      'ResourceType': 'volume',
      'Tags': [{
        'Key': 'Name',
        'Value': 'ansible-ec2-test'
      }]
    }, {
      'ResourceType': 'instance',
      'Tags': [{
        'Key': 'Name',
        'Value': 'ansible-ec2-test'
      }]
    }],
    'IamInstanceProfile': {
      'Arn': 'arn:aws:iam::111111111111:instance-profile/ansible-session-manager'
    },
    'InstanceType': 't3.small'
  },
  'failed': False
}
```
