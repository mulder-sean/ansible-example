# Ansible
> Written by Sean Mulder for demonstration

## Try it out
| Costs will occur for AWS account |  
|-|

At time of writing the example the following versions were used  
* Ansible 2.9.6 [Installation](https://docs.ansible.com/ansible/latest/installation_guide/index.html)  
* Python 3.8.5 [Installation](https://www.python.org/downloads/)  
* Ubuntu 20.04.2 LTS [Installation of WSL](https://ubuntu.com/tutorials/ubuntu-on-windows#1-overview)  
* Amazon AWS Account [Configuration](https://docs.ansible.com/ansible/latest/scenario_guides/guide_aws.html#)  
* Boto Configuration Profile [Configuration](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html)  

### To execute full example
> __Don't forget__ to setup your boto profiles __~/.aws/config__ and credentials profile __~/.aws/credentials__

```bash  
  export ANSIBLE_LIBRARY=.library  
  ansible-playbook execute_role.yml --extra-vars "role=example variables_file=test-data/static-data.yml"  
```  

### For independent role usage
See __README.md__ in respective roles  
* Each role can create and destroy
* Each role has test data for running independently
* When used all together they pass data from one role to another
