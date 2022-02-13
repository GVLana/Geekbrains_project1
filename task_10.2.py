from abc import ABC, abstractmethod


class Fabric(ABC):

    @abstractmethod
    def consumption(self):
        pass


class Coat(Fabric):

    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return round(self.v / 6.5 + 0.5, 2)

    def total_consumption(self, coats):
        total = 0
        for coat in coats:
            total += coat.consumption
        return total


class Suit(Fabric):

    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return round(self.h * 2 + 0.3, 2)

    def total_consumption(self, suits):
        total = 0
        for suit in suits:
            total += suit.consumption
        return total


coats = []
suits = []

while True:
    clothe = input("Enter type of close to calculate. Coat or Suit. To stop press '*': ")
    if clothe == '*':
        break
    elif clothe.lower() == 'coat':
        custom = Coat(float(input("Enter your size: ")))
        print(f"The amount of fabric needed for this coat is: {custom.consumption}.")
        coats.append(custom)
        print(f"The amount of fabric needed for all coats is: {custom.total_consumption(coats)}.")
    elif clothe.lower() == 'suit':
        custom = Suit(float(input("Enter your height in meters: ")))
        print(f"The amount of fabric needed for this suits is {custom.consumption}.")
        suits.append(custom)
        print(f"The amount of fabric needed for all suits is: {custom.total_consumption(suits)}.")
