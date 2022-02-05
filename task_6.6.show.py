from sys import argv

with open("bakery.csv", "r", encoding="utf-8") as bun_r:
    if 1 < len(argv) < 4 and [i for i in argv[1:] if i.isdigit()]:
        if len(argv) == 3:
            start, end = map(int, argv[1:])
            print(*(p for i, p in enumerate(bun_r) if start -1 <= i < end), sep="")
        else:
            print(*(p for i, p in enumerate(bun_r) if i >= int(argv[1]) - 1), sep="")
    else:
        print(bun_r.read())

