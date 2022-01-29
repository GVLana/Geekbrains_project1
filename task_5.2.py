
n = int(input("Enter number: "))

odd_generator = (num for num in range(1, n, 2))
print(next(odd_generator))
print(next(odd_generator))
print(next(odd_generator))
print(next(odd_generator))

# for x in odd_generator:
#     print (x)
