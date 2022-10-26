# Задача 3. Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть в списке.
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают
# Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

import random as r
def List_Rand():
    return [r.randint(1,11) for i in range (r.randint(1,11))]

def Quantity_Repeat_El(number):
    count = 0
    for i in range(len(number)):
        for j in range (i+1, len(number)):
            if number[i]==number[j]:
                count+=1
    return count

def Unique_El(numbers:list):
    return list(filter(lambda x: numbers.count(x) == 1, numbers))

list_numbers = List_Rand()
print(f'начальный список -> {list_numbers}')
print(f'количество совпадающих элементов -> {Quantity_Repeat_El(list_numbers)}')
print(f'список уникальных элементов -> {Unique_El(list_numbers)}')