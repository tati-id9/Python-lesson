# Задача 1. Создайте телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# Предусмотрите следующие функции для справочника:
# - новая запись;
# - вывод всего справочника;
# - поиск по имени;
# - экспорт справочника в форматы html, xml;
# - чтение данных из файла;
# - дополнительные функции по желанию
# Требуется реализовать минимум 3 инструмента для работы со справочником.

from tkinter import *

def Add_Contact():
    if eName.get()!= "" and eSurame.get !="" and ePhone.get() != "":
        new_contact = '{name} {surname}: {phone_number}'.format(name = eName.get(), surname = eSurame.get(), phone_number = ePhone.get())
        allContacts.insert(END, new_contact)
        Write_Contacts()
    else:
        print("Не введены данные")

def Write_Contacts():
    data = open('phonebook.txt', 'w', encoding='utf-8')
    for row in allContacts.get(0, END):
        data.writelines(row + '\n')
    data.close()

def Print_Contats():
    try:
        data = open('phonebook.txt', 'r', encoding='utf-8')
        for contact in data.readlines():
            allContacts.insert(END, contact)
        data.close()
    except FileNotFoundError:
        print("Файл не найден. Создайте файл")

def Search():
    liter = eP.get()
    file = open('phonebook.txt', encoding='utf-8')
    data = file.readlines()
    file.close()
    for i in range(len(data)):
        if liter in data[i]:
           labelТ1 = Label(root, text= "Найден: "+ data[i])
           labelТ1.grid(row=9, column=0)

root = Tk()
root.geometry('400x300')

buttonAddContact = Button(root, text="Добавить контакт", command= Add_Contact)
buttonAddContact.grid(row=3, column=0, columnspan=2)
buttonAddContact = Button(root, text="Поиск", command= Search)
buttonAddContact.grid(row=7, column=1, columnspan=2)

labelName = Label(root, text="Укажите имя")
labelName.grid(row=0, column=0)
labelSurame = Label(root, text="Укажите фамилию")
labelSurame.grid(row=1, column=0)
labelPhome = Label(root, text="Введите номер телефона")
labelPhome.grid(row=2, column=0)

eName = Entry(root, width=15)
eName.grid(row=0, column=1)
eSurame = Entry(root, width=15)
eSurame.grid(row=1, column=1)
ePhone = Entry(root, width=15)
ePhone.grid(row=2, column=1)
eP = Entry(root, width=45)
eP.grid(row=7, column=0)

allContacts =Listbox(root, height=8, width=45, selectmode=EXTENDED)
allContacts.grid(row=4, column=0)
Print_Contats()
root.mainloop()