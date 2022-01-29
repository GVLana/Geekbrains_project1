
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


for i in my_list:
    if i.isdigit() or i.isalnum() is False:
        if len(i) == 1:
            i = f'"{int(i):02}"'
        elif len(i) > 1 and i[0].isdigit() is False:
            i = f'"{i[0]}{int(i[1:]):02}"'
        elif i.isdigit() and len(i) > 1:
            i = f'"{i}"'
    print(i, end=" ")
