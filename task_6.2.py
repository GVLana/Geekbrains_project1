from collections import Counter


with open('tuple.txt', 'r', encoding='utf-8') as t:
    my_dict = Counter()
    for i in t:
        my_dict[i.split()[0]] += 1
    ip = my_dict.most_common(1)[0][0][1:]
    spam = my_dict.most_common(1)[0][1]
    print(f"Spammer ip is {ip} number of requests is {spam}.")
