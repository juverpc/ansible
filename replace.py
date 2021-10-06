import yaml
import os
import json

path_yaml_playbook = "./group_vars/tableau_servers.yml"
path_json_file = "./json_file.json"

def replace_tableau_values():
    with open (path_yaml_playbook) as f:
        file = yaml.safe_load(f)
    file['ansible_password'] = os.environ['VM_PASSWORD']
    
    with open(path_yaml_playbook, 'w') as f:
        result = yaml.dump(file, f)
    return ('values were replaced')

def replace_json_file():
    with open (path_json_file) as f:
        file = json.load(f)
    file['menu']['id'] = '12'

    with open (path_json_file, 'w') as f:
       json.dump(file, f)

if __name__ == "__main__":
    replace_json_file()
    replace_tableau_values()