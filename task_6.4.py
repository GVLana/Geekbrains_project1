from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as u:
    with open("hobby.csv", "r", encoding="utf-8") as h:
        info_sum = zip_longest(u, h, fillvalue=None)

        with open("info_about_user.txt", "w", encoding="utf-8") as i:
            for pair in info_sum:
                print(f"{str(pair[0]).strip()}: {str(pair[1])}\n", file=i)
