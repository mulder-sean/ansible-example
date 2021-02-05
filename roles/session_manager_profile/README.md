### Create
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=session_manager_profile variables_file=test-data/create.yml independent_test='true'"  
```  

### Destroy
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=session_manager_profile variables_file=test-data/destroy.yml  independent_test='true'"  
```  

### Output
Registers a global variable: __created_session_manager_role_info__ with output:
```python
{
  'changed': False,
  'iam_role': {
    'path': '/',
    'role_name': 'ansible-session-manager',
    'role_id': '111111111111111111111',
    'arn': 'arn:aws:iam::111111111111:role/ansible-session-manager',
    'create_date': '2021-02-03T23:04:10+00:00',
    'assume_role_policy_document': {
      'version': '2012-10-17',
      'statement': [{
        'effect': 'Allow',
        'principal': {
          'service': 'ec2.amazonaws.com'
        },
        'action': 'sts:AssumeRole'
      }]
    },
    'description': 'ansible-session-manager',
    'max_session_duration': 3600,
    'role_last_used': {},
    'attached_policies': [{
      'policy_name': 'ansible-session-manager',
      'policy_arn': 'arn:aws:iam::111111111111:policy/ansible-session-manager'
    }]
  },
  'path': '/',
  'role_name': 'ansible-session-manager',
  'role_id': '111111111111111111111',
  'arn': 'arn:aws:iam::111111111111:role/ansible-session-manager',
  'create_date': '2021-02-03T23:04:10+00:00',
  'assume_role_policy_document': {
    'version': '2012-10-17',
    'statement': [{
      'effect': 'Allow',
      'principal': {
        'service': 'ec2.amazonaws.com'
      },
      'action': 'sts:AssumeRole'
    }]
  },
  'description': 'ansible-session-manager',
  'max_session_duration': 3600,
  'role_last_used': {},
  'attached_policies': [{
    'policy_name': 'ansible-session-manager',
    'policy_arn': 'arn:aws:iam::111111111111:policy/ansible-session-manager'
  }],
  'uid': 0,
  'gid': 0,
  'owner': 'root',
  'group': 'root',
  'mode': '0755',
  'state': 'directory',
  'size': 4096,
  'failed': False
}
```
