
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        full_name = self.name + " " + self.surname
        return full_name

    def get_total_income(self):
        total_income = self._income.get("wage") + self._income.get("bonus")
        return total_income


employee_info = {}

while True:
    user_input = input("Press enter to start. For exit enter x: ")
    if user_input.lower() == 'x':
        break
    else:
        try:
            workers = Position(input("Enter employee name: "),
                               input("Enter employee surname: "),
                               input("Enter employee position: "),
                               int(input("Enter employee salary: ")),
                               int(input("Enter employee bonus: ")))
            print(workers.get_full_name())
            print(workers.get_total_income())
            print(workers._income)
            employee = {workers.get_full_name(): workers.get_total_income()}
        except ValueError:
            print(f"Check your input data and try again.")
            continue
        else:
            employee_info.update(employee)

print(employee_info)
