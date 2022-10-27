# Задача 3. Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть в списке.
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают
# Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

import list_rr

def Quantity_Repeat_El(number):
    count = 0
    for i in range(len(number)):
        if number.count(i) != 1:
            count+=number.count(i)
    return count

def Unique_El(list):
    for i in reversed(range(len(list))):
        if list[i] in list[:i]:
            del list[i]
    return list

list_numbers = list_rr.List_Rand()
print(f'начальный список -> {list_numbers}')
print(f'количество совпадающих элементов -> {Quantity_Repeat_El(list_numbers)}')
print(f'список уникальных элементов -> {Unique_El(list_numbers)}')