
class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} drove off."

    def stop(self):
        return f"{self.name} stopped."

    def turn(self):
        while True:
            direction = input("Enter r for right or l for left. To exit enter x. ")
            try:
                if direction.lower() == "x":
                    break
                elif direction.lower() == "r":
                    print(f"The car is turning right.")
                elif direction.lower() == "l":
                    print(f"The car is turning left")
                else:
                    raise ValueError("The command is not found.")
            except ValueError:
                print("The command not found. Try again.")
                continue
        return ""

    def show_speed(self):
        return f"Current speed of {self.name} is {self.speed}."


class TownCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"Over speed!"
        else:
            return f"Current speed of {self.name} is {self.speed}."


class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"Over speed!"
        else:
            return f"Current speed of {self.name} is {self.speed}."


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, True)


while True:
    user_input = input("Choose and enter your car type (town, sport, work, police). For exit enter x: ")
    if user_input.lower() == "x":
        break
    elif user_input.lower() == "town":
        town = TownCar(input("Car brand: ").capitalize(), input("Car color: "), int(input("Car speed: ")), False)
        print(town.go())
        print(town.show_speed())
        print(town.turn())
        print(town.stop())

    elif user_input.lower() == "sport":
        sport = SportCar(input("Car brand: ").capitalize(), input("Car color: "), int(input("Car speed: ")), False)
        print(sport.go())
        print(sport.show_speed())
        print(sport.turn())
        print(sport.stop())

    elif user_input.lower() == "work":
        work = WorkCar(input("Car brand: ").capitalize(), input("Car color: "), int(input("Car speed: ")), False)
        print(work.go())
        print(work.show_speed())
        print(work.turn())
        print(work.stop())

    elif user_input.lower() == "police":
        police = PoliceCar(input("Car brand: ").capitalize(), input("Car color: "), int(input("Car speed: ")))
        print(police.go())
        print(police.show_speed())
        print(police.turn())
        print(police.stop())
