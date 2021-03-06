from sys import argv

# with open("bakery.csv", "x", encoding="utf-8") as bun_x:
with open("bakery.csv", "a", encoding="utf-8") as bun_a:
    with open("bakery.csv", "r", encoding="utf-8") as bun_r:
        if len(argv) > 1 and [i for i in argv[1:] if "." in i and i.replace(".", "").isdigit()]:
            if round(float(argv[1]), 3) <= 99999.99:
                print(f"{round(float(argv[1]), 3):>010}", file=bun_a)
            else:
                print("Error. Number has to be less than 99 999,999")
        else:
            print(bun_r.read())
