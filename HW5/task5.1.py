# Задача 1. Задайте список случайных чисел от 1 до 10, 
# выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8


import list_rr
list_numbers = list_rr.List_Rand()

result = lambda x: x>5
result = list(filter(result, list_numbers))
print(f'начальный список -> {list_numbers}')
print(f'список с элементами больше 5 ->{result}')

