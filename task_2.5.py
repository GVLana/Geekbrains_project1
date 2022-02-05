
price_list = [57.8, 46.51, 97, 22, 10.00, 5.04]


for i in price_list:
    r, kk = f"{i:.2f}".split(".")
    print(f"{r} руб {kk} коп,", end=" ")


print(f"\nID of original price list: {id(price_list)}")
price_list.sort()
print(f"Sorted list: {price_list}")
print(f"ID of sorted prices in ascending order: {id(price_list)}")
new_list = sorted(price_list, reverse=True)
print(new_list)
print(f"ID of sorted prices in descending order: {id(new_list)}")