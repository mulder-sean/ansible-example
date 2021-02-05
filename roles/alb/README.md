### Create
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=alb variables_file=test-data/create.yml independent_test='true'"  
```  

### Destroy
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=alb variables_file=test-data/destroy.yml independent_test='true'"  
```  

### Output
Registers a global variable: __created_alb_info__ with output:
```python
{
  'changed': True,
  'load_balancer_arn': 'arn:aws:elasticloadbalancing:us-east-1:111111111111:loadbalancer/app/ansible-alb/57e0be4bc84a2187',
  'dns_name': 'ansible-alb-393631010.us-east-1.elb.amazonaws.com',
  'canonical_hosted_zone_id': '11111111111111',
  'created_time': '2021-02-04T20:12:20.830000+00:00',
  'load_balancer_name': 'ansible-alb',
  'scheme': 'internet-facing',
  'vpc_id': 'vpc-06b1fa12f16c2ccd6',
  'state': {
    'code': 'active'
  },
  'type': 'application',
  'availability_zones': [{
    'zone_name': 'us-east-1c',
    'subnet_id': 'subnet-0286f975a08726cfe',
    'load_balancer_addresses': []
  }, {
    'zone_name': 'us-east-1b',
    'subnet_id': 'subnet-09d27172cd4179362',
    'load_balancer_addresses': []
  }, {
    'zone_name': 'us-east-1a',
    'subnet_id': 'subnet-0c46d0f76d386ba74',
    'load_balancer_addresses': []
  }],
  'security_groups': ['sg-035e761328242ecbc'],
  'ip_address_type': 'ipv4',
  'tags': {
    'Name': 'ansible-alb'
  },
  'access_logs_s3_enabled': 'false',
  'access_logs_s3_bucket': 'alb_logs',
  'access_logs_s3_prefix': '',
  'idle_timeout_timeout_seconds': '60',
  'deletion_protection_enabled': 'false',
  'routing_http2_enabled': 'true',
  'routing_http_drop_invalid_header_fields_enabled': 'false',
  'routing_http_desync_mitigation_mode': 'defensive',
  'waf_fail_open_enabled': 'false',
  'listeners': [{
    'listener_arn': 'arn:aws:elasticloadbalancing:us-east-1:111111111111:listener/app/ansible-alb/57e0be4bc84a2187/f3ebad1c4ef1dea9',
    'load_balancer_arn': 'arn:aws:elasticloadbalancing:us-east-1:111111111111:loadbalancer/app/ansible-alb/57e0be4bc84a2187',
    'port': 80,
    'protocol': 'HTTP',
    'default_actions': [{
      'type': 'forward',
      'target_group_arn': 'arn:aws:elasticloadbalancing:us-east-1:111111111111:targetgroup/ansible-alb/ca8d4e1c881b04dc',
      'forward_config': {
        'target_groups': [{
          'target_group_arn': 'arn:aws:elasticloadbalancing:us-east-1:111111111111:targetgroup/ansible-alb/ca8d4e1c881b04dc',
          'weight': 1
        }],
        'target_group_stickiness_config': {
          'enabled': False
        }
      }
    }],
    'rules': [{
      'rule_arn': 'arn:aws:elasticloadbalancing:us-east-1:111111111111:listener-rule/app/ansible-alb/57e0be4bc84a2187/f3ebad1c4ef1dea9/b686ccdcca3e096f',
      'priority': 'default',
      'conditions': [],
      'actions': [{
        'type': 'forward',
        'target_group_arn': 'arn:aws:elasticloadbalancing:us-east-1:111111111111:targetgroup/ansible-alb/ca8d4e1c881b04dc',
        'forward_config': {
          'target_groups': [{
            'target_group_arn': 'arn:aws:elasticloadbalancing:us-east-1:111111111111:targetgroup/ansible-alb/ca8d4e1c881b04dc',
            'weight': 1
          }],
          'target_group_stickiness_config': {
            'enabled': False
          }
        }
      }],
      'is_default': True
    }]
  }],
  'failed': False
}
 ```
