### Create
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=security_groups variables_file=test-data/create.yml independent_test='true'"  
```  

### Destroy
As of 2020-02-03 the destroy fails because of the order of creation.
To properly delete you have to reverse the order but I did not code for that.

### Output
Registers a global variable: __created_public_security_group_info__ with output:
```python
{
  'changed': True,
  'description': 'ansible-public',
  'group_name': 'ansible-public',
  'ip_permissions': [{
    'from_port': 80,
    'ip_protocol': 'tcp',
    'ip_ranges': [{
      'cidr_ip': '0.0.0.0/0'
    }],
    'ipv6_ranges': [],
    'prefix_list_ids': [],
    'to_port': 80,
    'user_id_group_pairs': []
  }],
  'owner_id': '111111111111',
  'group_id': 'sg-0de4bd0331ba3d836',
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
    'Name': 'ansible-public'
  },
  'vpc_id': 'vpc-0adcd5ea40b2f5f89',
  'failed': False
}
```
