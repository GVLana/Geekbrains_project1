import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

jokes = []
user_input = int(input("Enter a number of jokes: "))


def get_jokes(n):
    x = 0
    while x in range(n):
        jokes.append(random.choice(nouns) + ' ' + random.choice(adverbs) + ' ' + random.choice(adjectives))
        x += 1
    return jokes


print(get_jokes(user_input))
