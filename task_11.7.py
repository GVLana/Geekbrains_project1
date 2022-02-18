class ComplexNumber:

    def __init__(self, a, b, *args):
        self.a = int(a)
        self.b = int(b)
        self.z = 'a + b * i'

    def __add__(self, other):
        return f"Sum is z = {self.a + other.a} + {self.b + other.b} * i"

    def __mul__(self, other):
        return f"The result of multiplication is z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a + self.a * other.b} * i"

    def __str__(self):
        return f"z = {self.a} + {self.b} * i"


while True:
    a1 = input("Enter a real number for 1st complex number: ")
    if a1 == "*":
        break
    b1 = input("Enter an imaginary number for 1st complex number: ")
    if b1 == "*":
        break
    a2 = input("Enter a real number for 2nd complex number: ")
    if a2 == "*":
        break
    b2 = input("Enter an imaginary number for 2nd complex number: ")
    if b2 == "*":
        break
    else:
        z1 = ComplexNumber(a1, b1)
        z2 = ComplexNumber(a2, b2)
        print(z1 + z2)
        print(z1 * z2)


