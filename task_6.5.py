from sys import argv
from itertools import zip_longest

user, hobby, file = argv[1:]

with open(fr"{user}\users.csv", "r", encoding="utf-8") as u:
    with open(fr"{hobby}\hobby.csv", "r", encoding="utf-8") as h:
        info_sum = zip_longest((" ".join(user.split(",")) for user in u), h, fillvalue=None)

        with open(fr"{file}\info_about_user.txt", "w", encoding="utf-8") as i:
            for pair in info_sum:
                print(f"{str(pair[0]).strip()}: {str(pair[1]).strip()}", file=i)
