name_dict = {}

employee_list = []

while True:
    user_input = input("Enter a name of employee. To stop press q: ")
    if user_input == 'q':
        break
    else:
        employee_list.append(user_input)
# print(employee_list)


def thesaurus_adv(*args):
    for i in employee_list:
        n, s = i.split()
        val = name_dict.setdefault(s[0].title(), {n[0].title(): [i.title()]})
        n_val = val.setdefault(n[0].title(), [i.title()])
        if i not in n_val:
            n_val.append(i.title())
    sorted_name_dict = dict(sorted(name_dict.items(), key=lambda x: x[0]))
    return sorted_name_dict


print(thesaurus_adv(employee_list))
