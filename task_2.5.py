
price_list = [57.8, 46.51, 97, 22, 10.00, 5.04]

for i in price_list:
    r, kk = f"{i:.2f}".split(".")
    print(f"{r} руб {kk} коп,", end=" ")
