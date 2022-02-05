
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    with open('tuple.txt', 'w', encoding='utf-8') as t:
        tuple_list = []
        for line in f:
            addr = line.split()[0]
            type = line.split()[5][1:]
            resource = line.split()[6]
            result = (addr, type, resource)
            tuple_list.append(result)
            t.writelines(f'{result}\n')
        for i in tuple_list:
            print(i)
