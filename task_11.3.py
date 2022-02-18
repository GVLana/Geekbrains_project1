class ListCheckForNumbers(Exception):

    def __init__(self, param):
        self.param = param


num_list = []

while True:
    try:
        user_input = input("Enter a number. For exit press '*': ")
        if user_input == "*":
            break
        else:
            el = int(user_input)
            if el is False:
                raise ValueError("You entered not a number. ")
    except ValueError:
        print("You entered not a number. ")
    else:
        num_list.append(el)
print(num_list)
