### Create
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=internet_gateway variables_file=test-data/create.yml independent_test='true'"  
```  

### Destroy
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=internet_gateway variables_file=test-data/destroy.yml  independent_test='true'"  
```  

### Output
Registers a global variable: __created_internet_gateway_info__ with output:
```python
{
  'changed': True,
  'gateway_id': 'igw-02db4fee12de35edd',
  'tags': {
    'Name': 'ansible-ig'
  },
  'vpc_id': 'vpc-0adcd5ea40b2f5f89',
  'failed': False
}
```
