""" Задача 2. В файле находятся названия фруктов. Выведите все фрукты,
названия которых начинаются на заданную букву.
а –> абрикос, авокадо, апельсин, айва. """

def Read_File():
    file = open("HW3/HW3_2/frukt.txt", encoding='utf-8')
    data = file.readlines()
    file.close()
    return data

def Get_Frukt(data, liter):
    df=[]
    for i in range(len(data)):
        if data[i][0].lower() == liter.lower():
            df.append(data[i])
    return df

liter = input("введите первую букву: ")
print(Get_Frukt(Read_File(), liter))
