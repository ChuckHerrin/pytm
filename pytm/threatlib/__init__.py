import os
import yaml

def load_threats():
    threats = []
    base_path = os.path.dirname(__file__)

    # Load built-in threats
    for filename in os.listdir(base_path):
        if filename.endswith('.yaml') and filename != 'custom':
            with open(os.path.join(base_path, filename), 'r') as f:
                threats.extend(yaml.safe_load(f))

    # Load custom threats
    custom_path = os.path.join(base_path, 'custom')
    if os.path.exists(custom_path):
        for filename in os.listdir(custom_path):
            if filename.endswith('.yaml'):
                with open(os.path.join(custom_path, filename), 'r') as f:
                    threats.extend(yaml.safe_load(f))

    return threats
