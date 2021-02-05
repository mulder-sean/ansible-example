### Create
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=route_tables variables_file=test-data/create.yml independent_test='true'"  
```  

### Destroy
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=route_tables variables_file=test-data/destroy.yml independent_test='true'"  
```  

### Output
Registers a global variable: __built_nat_subnet_mapping__ with output:
```python
{
  'changed': True,
  'results': [{
    'zone': 'us-east-1a',
    'public_subnets': ['subnet-04c343400c292c0e2'],
    'private_subnets': ['subnet-049de2d67e21a5ec0'],
    'nat_gateway_id': 'nat-070612b08088176b9'
  }],
  'failed': False
}
```

Registers a global variable: __created_public_route_info__ with output:
```python
{
  'changed': False,
  'route_table': {
    'associations': [{
      'main': False,
      'route_table_association_id': 'rtbassoc-08cb4c2f5a12c0ced',
      'route_table_id': 'rtb-0f41051ea2aa87037',
      'subnet_id': 'subnet-04c343400c292c0e2',
      'association_state': {
        'state': 'associated'
      }
    }],
    'propagating_vgws': [],
    'route_table_id': 'rtb-0f41051ea2aa87037',
    'routes': [{
      'destination_cidr_block': '10.20.0.0/17',
      'gateway_id': 'local',
      'origin': 'CreateRouteTable',
      'state': 'active'
    }, {
      'destination_cidr_block': '0.0.0.0/0',
      'gateway_id': 'igw-01f3349fdf9cba9bc',
      'origin': 'CreateRoute',
      'state': 'active'
    }],
    'tags': {
      'Name': 'ansible-public'
    },
    'vpc_id': 'vpc-0adcd5ea40b2f5f89',
    'owner_id': '111111111111',
    'id': 'rtb-0f41051ea2aa87037'
  },
  'failed': False
}
```

Registers a global variable: __created_private_route_info__ with output:
```python
{
  'results': [{
    'changed': False,
    'route_table': {
      'associations': [{
        'main': False,
        'route_table_association_id': 'rtbassoc-0af9724810182dce4',
        'route_table_id': 'rtb-03e8af0f651774c9c',
        'subnet_id': 'subnet-049de2d67e21a5ec0',
        'association_state': {
          'state': 'associated'
        }
      }],
      'propagating_vgws': [],
      'route_table_id': 'rtb-03e8af0f651774c9c',
      'routes': [{
        'destination_cidr_block': '10.20.0.0/17',
        'gateway_id': 'local',
        'origin': 'CreateRouteTable',
        'state': 'active'
      }, {
        'destination_cidr_block': '0.0.0.0/0',
        'nat_gateway_id': 'nat-070612b08088176b9',
        'origin': 'CreateRoute',
        'state': 'active'
      }],
      'tags': {
        'Name': 'private-us-east-1a'
      },
      'vpc_id': 'vpc-0adcd5ea40b2f5f89',
      'owner_id': '111111111111',
      'id': 'rtb-03e8af0f651774c9c'
    },
    'invocation': {
      'module_args': {
        'profile': 'default',
        'routes': [{
          'destination_cidr_block': '0.0.0.0/0',
          'nat_gateway_id': 'nat-070612b08088176b9'
        }],
        'state': 'present',
        'subnets': ['subnet-049de2d67e21a5ec0'],
        'tags': {
          'Name': 'private-us-east-1a'
        },
        'vpc_id': 'vpc-0adcd5ea40b2f5f89',
        'debug_botocore_endpoint_logs': False,
        'validate_certs': True,
        'lookup': 'tag',
        'purge_routes': True,
        'purge_subnets': True,
        'purge_tags': False,
        'ec2_url': None,
        'aws_secret_key': None,
        'aws_access_key': None,
        'security_token': None,
        'region': None,
        'propagating_vgw_ids': None,
        'route_table_id': None
      }
    },
    'failed': False,
    'mpr': {
      'zone': 'us-east-1a',
      'public_subnets': ['subnet-04c343400c292c0e2'],
      'private_subnets': ['subnet-049de2d67e21a5ec0'],
      'nat_gateway_id': 'nat-070612b08088176b9'
    },
    'ansible_loop_var': 'mpr'
  }],
  'msg': 'All items completed',
  'changed': False
}
```
