""" Задача 1. Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N.
60 -> 2, 2, 3, 5 """

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def Get_Diviger (number):
    diviger = []
    for i in range(2, number//2):
        while IsPrime(i) and number%i==0:
            diviger.append(i)
            number/=i
    return diviger
    
n = int(input("введите n = "))
print(Get_Diviger(n)) 