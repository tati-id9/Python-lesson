
dictionary = \
    {
        'Привет': 'Салют',
        'Как тебя зовут?': 'меня зовут Бот',
        'Стоп': 'Увидимся'
    }

def Boot():
    start = True
    while start:
        user_wr = input("user: ")
        if user_wr == 'Стоп':
            start = not start
        if user_wr in dictionary.keys():
            print ('Бот:', dictionary[user_wr])
        else:
            print ('Бот: я не знаю о чем ты')
