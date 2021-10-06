import yaml
import re
import os

path_yaml_playbook = "./playbook.yml"

def replace_playbook_values():
    read = yaml.safe_load(open(path_yaml_playbook ))
    read[0]['tasks'][0]['win_user']['name'] = 'Test'
    read[0]['tasks'][0]['win_user']['password'] = os.environ['VM_PASSWORD']
    result = yaml.dump(read)
    print (result)

if __name__ == "__main__":
    replace_playbook_values()