import telebot

# Укажите ваш токен бота, который можно получить у BotFather
TOKEN = '7662314218:AAEWqpenz2BgVap2csEHbfmskeuVDH5X3WE'

bot = telebot.TeleBot(TOKEN)


# Ответ на команду "/start"
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Задай мне вопрос!")


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Преобразуем сообщение в нижний регистр для упрощения обработки
    text = message.text

    bot.reply_to(message, text)

# Запуск бота
bot.polling()
