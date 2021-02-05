### Create
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=alb_target_group variables_file=test-data/create.yml independent_test='true'"  
```  

### Destroy
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=alb_target_group variables_file=test-data/destroy.yml  independent_test='true'"  
```  

### Output
Registers a global variable: __created_alb_target_group_info__ with output:
```python
{
  'changed': True,
  'target_group_arn': 'arn:aws:elasticloadbalancing:us-east-1:111111111111:targetgroup/ansible-alb/0e8aa58bd94078e0',
  'target_group_name': 'ansible-alb',
  'protocol': 'HTTP',
  'port': 8080,
  'vpc_id': 'vpc-06b1fa12f16c2ccd6',
  'health_check_protocol': 'HTTP',
  'health_check_port': '8080',
  'health_check_enabled': True,
  'health_check_interval_seconds': 30,
  'health_check_timeout_seconds': 5,
  'healthy_threshold_count': 2,
  'unhealthy_threshold_count': 2,
  'health_check_path': '/',
  'matcher': {
    'http_code': '200'
  },
  'load_balancer_arns': [],
  'target_type': 'instance',
  'protocol_version': 'HTTP1',
  'stickiness_enabled': 'false',
  'deregistration_delay_timeout_seconds': '300',
  'stickiness_type': 'lb_cookie',
  'stickiness_lb_cookie_duration_seconds': '86400',
  'slow_start_duration_seconds': '0',
  'load_balancing_algorithm_type': 'round_robin',
  'tags': {
    'Name': 'ansible-alb'
  },
  'failed': False
}
 ```
