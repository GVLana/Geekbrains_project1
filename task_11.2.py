class DivisionByZero(Exception):

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def check_division(self):
        try:
            dividend = int(self.param1)
            divider = int(self.param2)
            if divider == 0:
                raise ZeroDivisionError("You can't divide by zero.")
        except ValueError:
            print("You enter not a number. ")
        except ZeroDivisionError:
            print("You can't divide by zero. ")
        else:
            return round(dividend / divider, 2)


while True:
    user_input_1 = input("Enter dividend. For exit press *: ")
    if user_input_1 == "*":
        break
    user_input_2 = input("Enter divider. For exit press *: ")
    if user_input_2 == "*":
        break
    else:
        division = DivisionByZero(user_input_1, user_input_2)
        result = DivisionByZero.check_division(division)
        print(result)
