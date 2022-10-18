""" Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
6 –> 1 1 2 3 5 8 """
def Fibonacci(n):
    list_fib = [1,1]
    for i in range(2, n):
        list_fib.append(list_fib[i-1]+list_fib[i-2])
    return list_fib
 
n = int(input("введите n = "))
list_fibonacci = Fibonacci(n)

file = open("fbonacci.txt", "w")
print(*list_fibonacci, file=file, sep=", ")
file.close()
