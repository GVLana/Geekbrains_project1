from datetime import datetime
import calendar


class Date:

    def __init__(self, string):
        self.string = string

    @classmethod
    def convert_into_integer(cls, string):
        date_list = list(map(int, string.split('-')))
        return date_list

    @staticmethod
    def date_check(my_list):
        month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if my_list[0] > 31 or my_list[0] < 1:
            return f"Day is not valid. "
        else:
            if my_list[1] not in month:
                return f"Month is not valid. "
            else:
                if my_list[0] > month[my_list[1]]:
                    return f"Day is not valid"
                else:
                    if my_list[2] < 0 or my_list[2] > datetime.now().year:
                        return f"Year is not valid. "
                    else:
                        if my_list[1] == 2 and my_list[0] == 29:
                            if calendar.isleap(my_list[2]) is False:
                                return f"Day is not valid. This is not a leap year. "
        return "-".join(map(str, my_list))


while True:
    user_input = input("Enter a date in the format 'dd-mm-yyyy'. For exit press *: ")
    if user_input == "*":
        break
    else:
        date = Date.convert_into_integer(user_input)
        checked_date = Date.date_check(date)
        print(checked_date)
