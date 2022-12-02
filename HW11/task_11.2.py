# Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома 
# и список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. 
# метров, цены от 3 до 20 млн.
import random as r
import matplotlib.pyplot as plt

metric = 50000

cost = list(r.randint(3000000, 20000000) for i in range(15))
print (f'стоимость домов - > {cost}')
square = list(r.randint(100, 300) for i in range(15))
print (f'площадь домов - > {square}')

square_meter = []
for i in range(15):
    square_meter.append(cost[i]/square[i])
print (f'стоимость квадратноного метра - > {square_meter}')

plt.subplot(111)
plt.bar(list(range(1,16)), square_meter)
plt.xlabel("дом")
plt.ylabel("стоимость квадратноного метра")
plt.show()

houses = list(zip(square, cost, square_meter))
houses = list(filter(lambda x: x[2]<metric, houses))
result = sorted(houses, key=lambda x: x[0])
print(f'массив домов отсортированных по площади, у которых стоимость квадратного метра меньше 50000 -> {result}')

