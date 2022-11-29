# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

import math as m

lis = []
for i  in range (2, 12):
    for j in range (1, i):
        if m.gcd(i, j) == 1:
            lis.append(f'{j}/{i}')

print(lis)