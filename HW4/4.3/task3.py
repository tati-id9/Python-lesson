""" Задача 3. Выведите число π с заданной точностью. 
Точность вводится пользователем в виде натурального числа.
3 -> 3.142
5 -> 3.14159 """

import math as m
n = int(input("введите точность = "))
print(round(m.pi, n))