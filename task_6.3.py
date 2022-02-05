from json import dump
from itertools import zip_longest

info_dict = {}

with open('users.csv', 'r', encoding='utf-8') as u:
    with open('hobby.csv', 'r', encoding='utf-8') as h:
        if len(u.readlines()) >= len(h.readlines()):
            u.seek(0)
            h.seek(0)

            with open('info.txt', 'w', encoding='utf-8') as i:
                info_sum = zip_longest((" ".join(user.split(",")) for user in u), h, fillvalue=None)
                info_dict = {str(pair[0]).strip(): str(pair[1]).strip() for pair in info_sum}
                dump(info_dict, i, ensure_ascii=False, indent=4)
            print(info_dict)
        else:
            exit(1)
