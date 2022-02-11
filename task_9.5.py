class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки."


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"You picked up {self.title}."


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Now you can use {self.title} to draw."


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"{self.title} is available for drawing."


start = Stationery(input("Press enter to start: "))
print(start.draw())
while True:
    user_input = input("Choose a stationary. To stop enter x: ").lower()
    if user_input == "x":
        break
    elif user_input == "pen":
        pen = Pen(user_input.capitalize())
        print(pen.draw())

    elif user_input == "pencil":
        pencil = Pencil(user_input.capitalize())
        print(pencil.draw())

    elif user_input == "handle":
        handle = Handle(user_input.capitalize())
        print(handle.draw())
