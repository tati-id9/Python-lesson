# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
# Каждому месяцу соответствует своя строка. 
# Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты.
import random as r
dictionary = \
    {
        0: 'май',
        1: 'июнь',
        2: 'июль',
        3: 'август',
        4: 'сентябрь'
    }

size = 5
mas = [0] * size
for i in range (size):
    mas[i] = list(r.randint(0,35) for j in range(r.randint(30,31)))

mas2=[]
max_ave=0
k=-1
i_n=0 #индекс по строке начала промежутка
i_k=0 #индекс по столбцу начала промежутка
j_n=0 #индекс по строке конца промежутка
j_k=0 #индекс по столбцу конца промежутка

print("Матрица дней: ")
for i in range(0, len(mas)):
    for i2 in range(0, len(mas[i])):
        print(mas[i][i2], end=' ')
    print()
print()

for i in range(0, len(mas)):
    for j in range(0, len(mas[i])):
        mas2.append(mas[i][j])
        k+=1
        if k>6:
            ave=(mas2[k]+mas2[k-1]+mas2[k-2]+mas2[k-3]+mas2[k-4]+mas2[k-5]+mas2[k-6])/7
            if ave>max_ave:
                max_ave=ave
                i_k=i
                j_k=j
                if j<6:
                    i_n=i-1
                    j_n=len(mas[i_n])-(6-j)
                else:
                    i_n=i
                    j_n=j-6
                    
print ('7 дневный промежуток')
print (f'Начало промежутка - месяц: {dictionary[i_n]} (строка в матрице {i_n+1}), день: {j_n+1}')
print (f'Конец промежутка - месяц: {dictionary[i_k]} (строка в матрице {i_k+1}), день: {j_k+1}')
print (f'Максимальная средняя температура -> {round(max_ave, 2)}')