
name_dict = {}

employee_list = []

while True:
    user_input = input("Enter a name of employee. To stop press q: ")
    if user_input == 'q':
        break
    else:
        employee_list.append(user_input)
print(employee_list)


def thesaurus(x):
    for i in employee_list:
        key = i[0].title()
        if key in name_dict:
            name_dict[key] += [i.title()]
        else:
            name_dict[key] = [i.title()]
    sorted_name_dict = dict(sorted(name_dict.items(), key=lambda x: x[0]))
    return sorted_name_dict

print(thesaurus(employee_list))
