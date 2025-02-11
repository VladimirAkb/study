import telebot
import random
from telebot import types

user_score = 0
comp_score = 0

API_TOKEN = '7662314218:AAEWqpenz2BgVap2csEHbfmskeuVDH5X3WE'

# Инициализация бота
bot = telebot.TeleBot(API_TOKEN)

# Функция для получения случайного выбора компьютера
def get_computer_choice():
    return random.choice(["камень", "ножницы", "бумага"])

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Я Телеграм-бот. Напиши /help, чтобы узнать, что я умею.")

# Команда /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Я поддерживаю следующие команды:\n/start - Приветственное сообщение\n/help - Справка\n/game - Игра 'Камень, ножницы, бумага'")

# Команда /game
@bot.message_handler(commands=['game'])
def send_help(message):
    bot.reply_to(message, "Начнем игру. ")

    @bot.message_handler(func=lambda message: True)
    if message.text == "1":
        bot.reply_to(message, "камень")




bot.polling(none_stop=True)


