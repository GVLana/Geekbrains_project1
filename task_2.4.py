# import random

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# name_list = []
#
#
# for i in my_list:
#     name = i.split(" ").pop(-1).capitalize()
#     name_list.append(name)
#
# user_input = input("Enter your phrase: ")
# print(f"{user_input}, {random.choice(name_list)}.")

user_input = input("Enter your phrase: ")

for i in my_list:
    name = i.split(" ").pop(-1).capitalize()
    print(f"{user_input}, {name}.")
