
numbs = {11, 12, 13, 14}

for i in range(1, 101):
    if i in numbs:
        print(f"{i} процентов.")
    elif i % 10 == 1:
        print(f"{i} процент.")
    elif i % 10 > 1 and i % 10 < 5:
        print(f"{i} процента.")
    else:
        print(f"{i} процентов.")
END