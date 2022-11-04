# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
# in
# Number of words: -1
# out
# The data is incorrect
from random import randint, sample


def create(characters, n):
    if n <= 0:
        exit(print('Неверные данные'))
    else:
        return [''.join(sample(characters, len(characters))) for i in range(n)]


characters = ['а', 'б', 'в']
words = create(characters, int(input("Введите число слов: ")))
print(words)
words = list(filter(lambda a: a != 'абв', words))
print(words)
