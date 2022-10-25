""" Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы """

import random as r
list = [r.randint(1, 11)]
n = r.randint(0, 10)
for i in range(1, n):
    list.append(r.randint(1, 11))
print(f'список -> {list}')