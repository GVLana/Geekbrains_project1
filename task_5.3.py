
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Максим', 'Станислав']

klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


# tuple_generator = ((x, y) for x, y in zip(tutors, klasses))
# # print(type(tuple_generator))
# # print(type(next(tuple_generator)), next(tuple_generator))
#
# for i in tuple_generator:
#     print(i)


def t_generator():
    i = 0
    j = 0
    for x, y in zip(tutors[j], klasses[i]):
        while j < len(tutors):
            if j >= len(klasses):
                yield tutors[j], None
                i += 1
                j += 1
            else:
                yield tutors[j], klasses[i]
                i += 1
                j += 1


for u in t_generator():
    print(u)

print(type(t_generator()))
