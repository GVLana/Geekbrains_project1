
def odd_generator(num):
    for num in range(1, n, 2):
        yield num


n = int(input("Enter number: "))
odd_to = odd_generator(n)

print(next(odd_to))
print(next(odd_to))
print(next(odd_to))
print(next(odd_to))
print(next(odd_to))
print(next(odd_to))
print(next(odd_to))
print(next(odd_to))
