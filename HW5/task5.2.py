# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, 
# описывающие возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

import random as r
def List_Rand():
    return [r.randint(1,11) for i in range (r.randint(1,11))]

def Filter_Elements(numbers):
    list_result = [numbers[0]]
    for element in numbers:
        if element > list_result[-1]:
            list_result.append(element)
    return list_result

list_numbers = List_Rand()
print(f'начальный список -> {list_numbers}')
print(f'результат -> {Filter_Elements(list_numbers)}')

