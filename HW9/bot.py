#https://pypi.org/project/pyTelegramBotAPI/
import telebot

import random

bot = telebot.TeleBot("", parse_mode=None)

@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
	bot.reply_to(message, "Я могу с тобой сыграть, напиши /game")

#Игра угадай число
@bot.message_handler(commands=['game'])
def start(message):
    rnumber = random.randint(1, 1000)
    bot.send_message(message.chat.id, 'Отгадайте число от 1 до 1000')
    bot.register_next_step_handler(message, get_number, 1, rnumber)


def get_number(message, try_num: int, right_num: int):
    if message.text.isdigit():
        if right_num == int(message.text):
            bot.send_message(message.chat.id, 'Вы отгадали число! Количество попыток' + " " + str(try_num))
        else:
            if right_num < int(message.text):
                bot.send_message(message.chat.id, 'Загаданное число меньше введенного.')
            else:
                bot.send_message(message.chat.id, 'Загаданное число больше введенного.')
            bot.register_next_step_handler(message, get_number, try_num + 1, right_num)

    else:
        bot.send_message(message.chat.id, 'Вы ввели не число. Попробуйте еще раз.')
        bot.register_next_step_handler(message, get_number, try_num, right_num)


bot.infinity_polling()