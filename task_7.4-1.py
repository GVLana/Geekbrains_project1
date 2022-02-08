import os
from collections import defaultdict
import django

def get_info():
    root_dir = django.__path__[0]
    django_files = defaultdict(int)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            django_files[size] += 1
    for size, nums in sorted(django_files.items()):
        print(f'{size}: {nums}')

get_info()
