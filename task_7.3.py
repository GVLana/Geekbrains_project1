import os
import shutil

data = 'my_project'

try:
    for root, dirs, files in os.walk(data):
        if 'templates' in dirs and root != data:
            for i in os.listdir(os.path.join(root, 'templates')):
                shutil.copytree(os.path.join(root, 'templates', i), os.path.join(data, 'templates', i))
except FileExistsError as f:
    print(f"An error occured: {f}.")
    raise FileExistsError