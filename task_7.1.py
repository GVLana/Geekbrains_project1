import os
import yaml

# Проба создания структуры папок для себя:

m_template = ['base.html', 'index.html']
a_template = ['base.html', 'index.html']
mainapp = {'mainapp': m_template}
authapp = {'authapp': a_template}
a_template = {'authnapp': ['base.html', 'index.html']}
settings_template = ['__init__.py', 'dev.py', 'prod.py']
mainapp_template = ['__init__.py', 'models.py', 'views.py', {'templates': [mainapp]}]
authapp_template = ['__init__.py', 'models.py', 'views.py', {'templates': [authapp]}]


set = {'settings': settings_template}
main = {'mainapp': mainapp_template}
auth = {'authapp': authapp_template}


to_yaml = {'my_project': [set, main, auth]}

with open('config.yaml', 'w') as f:
    yaml.dump(to_yaml, f, default_style=False)

with open('config.yaml') as f:
    print(f.read())


starter = {'my_project': [{'settings': []}, {'mainapp': []}, {'authapp': []}]}

# Само выполнение Задания №1:

get_starter = [os.makedirs(os.path.join(k1, k2)) for k1, v1 in starter.items() if not os.path.exists(k1) for i in v1 for k2 in i.keys()]

