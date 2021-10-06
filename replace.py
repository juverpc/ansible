import yaml
import re
import os

path_yaml_playbook = "./group_vars/tableau_servers.yml"

# def replace_playbook_values():
#     read = yaml.safe_load(open(path_yaml_playbook ))
#     read[0]['tasks'][0]['win_user']['name'] = 'Test'
#     read[0]['tasks'][0]['win_user']['password'] = os.environ['VM_PASSWORD']
#     result = yaml.dump(read)
#     print (result)

# def replace_playbook_values():
#     with open (path_yaml_playbook) as f:
#         file = yaml.safe_load(f)
#     file[0]['tasks'][0]['win_user']['name'] = 'Test'
#     file[0]['tasks'][0]['win_user']['password'] = os.environ['VM_PASSWORD']

def replace_tableau_values():
    with open (path_yaml_playbook) as f:
        file = yaml.safe_load(f)
    file['ansible_password'] = os.environ['VM_PASSWORD']
    
    with open(path_yaml_playbook, 'w') as f:
        result = yaml.dump(file, f)
    print (result)

if __name__ == "__main__":
    replace_tableau_values()