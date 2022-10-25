""" Задача 2. В первой строке файла находится информация об ассортименте мороженного, 
во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, 
который закончился.
1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
2. «Сливочное», «Вафелька», «Сладкоежка»
Закончилось: «Бурёнка» """

from unittest import result


def Read_File():
    file = open("HW4/4.2/stock.txt", "r", encoding='utf-8')
    data = file.readlines()
    file.close()
    return data

def Finished_Goods(data):
    first = set(data[0].replace("\n", "").split(", "))
    second = set(data[1].replace("\n", "").split(", "))
    ended = first.difference(second)
    return ended

print(Finished_Goods(Read_File()))