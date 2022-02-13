
class Cell:
    def __init__(self, param):
        self.param = int(param)

    def __str__(self):
        return f'{self.param}'

    def __add__(self, other):
        return Cell(self.param + other.param)

    def __sub__(self, other):
        if self.param - other.param > 0:
            return Cell(self.param - other.param)
        else:
            print(f"The result cannot be negative.")
            return " "

    def __mul__(self, other):
        return Cell(self.param * other.param)

    def __truediv__(self, other):
        return Cell(self.param // other.param)

    def make_order(self, count_cell):
        row = ""
        for i in range(self.param // count_cell):
            row += "*" * count_cell + '\\n'
        row += "*" * (self.param % count_cell)
        return row


cell_1 = Cell(int(input("Enter a number of cells_1: ")))
order_cell_1 = int(input("Enter a number of cells in a row for cells_1: "))

cell_2 = Cell(int(input("Enter a number of cells_2: ")))
order_cell_2 = int(input("Enter a number of cells in a row for cells_2: "))

print(cell_1.make_order(order_cell_1))
print(cell_2.make_order(order_cell_2))
print(cell_1 + cell_2)
print((cell_1 - cell_2))
print(cell_1 * cell_2)
print((cell_1 / cell_2))
