
rus_num = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
           'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
           'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


user_input = input("Enter a number on English from 0 to 10: ")

def num_translated(x):
   result = rus_num.get(x.lower())
   return result

print(num_translated(user_input))

