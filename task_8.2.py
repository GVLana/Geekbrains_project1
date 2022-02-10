import re

output = re.compile(r'^(\b.+\b).*\[(.+)].*\"([A-Z]+) +(/.+?)\s.*?\" (\d+) (\d+) .*$|^$')
# output = re.compile(r'^(\b.+\b).*\[(.{1,})].*\"([A-Z]{1,}) +(/.+?)\s.*?\" (\d+) (\d+) .*$|^$')

with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        print(re.findall(output, line))
