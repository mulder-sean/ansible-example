### Create
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=nat_gateways variables_file=test-data/create.yml independent_test='true'"  
```  

### Destroy
Destroy does not work with nat gateways because it requires an additional input and logic to include nat_gateway_id.

### Output
Registers a global variable: __created_nat_gateways_info__ with output:
```python
{
  'results': [{
    'msg': '',
    'success': True,
    'changed': True,
    'create_time': '2021-02-03T18:19:34+00:00',
    'nat_gateway_addresses': [{
      'allocation_id': 'eipalloc-01413ef9ba59b04d6'
    }],
    'nat_gateway_id': 'nat-070612b08088176b9',
    'state': 'pending',
    'subnet_id': 'subnet-04c343400c292c0e2',
    'vpc_id': 'vpc-0adcd5ea40b2f5f89',
    'invocation': {
      'module_args': {
        'profile': 'default',
        'if_exist_do_not_create': True,
        'state': 'present',
        'subnet_id': 'subnet-04c343400c292c0e2',
        'debug_botocore_endpoint_logs': False,
        'validate_certs': True,
        'wait': False,
        'wait_timeout': 320,
        'release_eip': False,
        'ec2_url': None,
        'aws_secret_key': None,
        'aws_access_key': None,
        'security_token': None,
        'region': None,
        'eip_address': None,
        'allocation_id': None,
        'nat_gateway_id': None,
        'client_token': None
      }
    },
    'failed': False,
    'csb_info': {
      'subnet': {
        'map_public_ip_on_launch': True,
        'id': 'subnet-04c343400c292c0e2'
      }
    },
    'ansible_loop_var': 'csb_info'
  }, {
    'changed': False,
    'skipped': True,
    'skip_reason': 'Conditional result was False',
    'csb_info': {
      'subnet': {
        'map_public_ip_on_launch': False,
        'id': 'subnet-049de2d67e21a5ec0'
      }
    },
    'ansible_loop_var': 'csb_info'
  }],
  'changed': True,
  'msg': 'All items completed'
}
```
