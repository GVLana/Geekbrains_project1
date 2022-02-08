import os
import yaml
from yaml.loader import SafeLoader

with open('config.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)

def run_yalm(value, prefix=""):
    for dir, path in value.items():
        dir_path = os.path.join(prefix, dir)
        os.makedirs(dir_path, exist_ok=True)
        if isinstance(path, dict):
            run_yalm(path, dir_path)
        else:
            for i in path:
                if isinstance(i, dict):
                    run_yalm(i, dir_path)
                elif isinstance(i, str):
                    with open(os.path.join(dir_path, f'{i}'), 'w') as _:
                        pass

run_yalm(data)