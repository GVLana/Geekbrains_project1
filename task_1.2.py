
num_list = []

while True:
    uneven_num = int(input("Enter an uneven number from 1 to 1000. To stop press 0: "))
    if uneven_num == 0:
        break
    else:
        num_list.append(uneven_num ** 3)
print(num_list)


new_list = []
total = 0
for i in num_list:
    x = sum([int(j) for j in str(i)])
    if x % 7 == 0:
        new_list.append(x)
        total = sum(new_list)
        if total == 0:
            print(f"There is no uneven numbers multiples of 7.")
        else:
            print(f"The sum of uneven numbers multiples of 7 is: {total}")


num_list = list(map(lambda z: z + 17, num_list))
print(f"The new list is: {num_list}")

new_total = sum(i for i in num_list if i % 7 == 0)
if new_total == 0:
    print(f"There is no uneven numbers multiples of 7.")
else:
    print(f"The sum of uneven numbers multiples of 7 is: {new_total}")

