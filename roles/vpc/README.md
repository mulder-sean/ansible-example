### Create
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=vpc variables_file=test-data/create.yml independent_test='true'"  
```  

### Destroy
```bash  
  ansible-playbook execute_role.yml --extra-vars "role=vpc variables_file=test-data/destroy.yml  independent_test='true'"  
```  

### Output
Registers a global variable: __created_vpc_info__ with output:
```python
{
    "changed": False,
    "vpc": {
        "cidr_block": "10.20.0.0/17",
        "dhcp_options_id": "dopt-6f059a15",
        "state": "available",
        "owner_id": "111111111111",
        "instance_tenancy": "default",
        "cidr_block_association_set": [
            {
                "association_id": "vpc-cidr-assoc-01fe1c26e8f8f7370",
                "cidr_block": "10.20.0.0/17",
                "cidr_block_state": {"state": "associated"},
            }
        ],
        "is_default": False,
        "tags": {"Name": "ansible-example"},
        "classic_link_enabled": False,
        "id": "vpc-0536b48546f6b0bbc",
    },
    "failed": False,
}
 ```
