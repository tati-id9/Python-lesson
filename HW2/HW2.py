""" Задача 1. Напишите программу, которая принимает на вход число N 
и выдает список факториалов для чисел от 1 до N.
N = 4 -> [ 1, 2, 6, 24 ] (1, 1x2, 1x2x3, 1x2x3x4) """

import math

def Get_Factorial(x):
  factor = []
  if x == 0:
    factor.append(1)
  else:
    for i in range(1, x+1):
      factor.append(math.factorial(i))
      i+=1
  return factor

n = int(input("введите n = "))
print(*Get_Factorial(n), sep=', ')

""" Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z. """

print ("x | y | z | ¬(X ∧ Y) ∨ Z")
for x in range(0,2):
  for y in range(0,2):
    for z in range(0,2):
      bool_value = not(x and y) or z
      print("-   -   -   -")
      print(f'{x} | {y} | {z} | {int(bool_value)}')

""" Задача 3. Даны две строки. 
Посчитайте сколько раз каждый символ первой строки встречается во второй
«one» «onetwonine» - o – 2, n – 3, e – 2 """

s1=input("введите первую строку: ")
s2=input("введите вторую строку: ")

for i in range(0, len(s1)):
  print(f"{s1[i]} - {s2.count(s1[i])}")

""" Задача 4. Задайте список из N элементов, 
заполненных числами из промежутка [-N, N]. 
Сдвиньте все элементы списка на 2 позиции вправо.
3 -> [2, 3, -3, -2, -1, 0, 1] """

def List_Completion (n):
  list_n_number = []
  for i in range(-n,n+1):
    list_n_number.append(i)
  return list_n_number

def List_Shift (list_n, shift):
  list_n = list_n[-shift:] + list_n[:-shift]
  return list_n

n = int(input("введите n = "))
shift = int(input("введите сдвиг вправо = "))

print(*List_Shift(List_Completion (n), shift), sep=', ')