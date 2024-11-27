import telebot
from transliterate import translit

# Замените 'YOUR_BOT_TOKEN' на ваш реальный токен
API_TOKEN = '7662314218:AAEWqpenz2BgVap2csEHbfmskeuVDH5X3WE'

bot = telebot.TeleBot(API_TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram-бот. Я могу помочь тебе с транслитерацией. Напиши /help, чтобы узнать, что я умею.")

# Команда /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Я поддерживаю следующие команды:\n/start - Приветственное сообщение\n/help - Справка\n/trans <текст> - Транслитерация текста с кириллицы на латиницу.")

# Команда /trans для транслитерации
@bot.message_handler(commands=['trans'])
def transliterate_text(message):
    text = message.text[7:]  # Убираем команду '/trans ' из текста
    if text:
        transliterated_text = translit(text, 'ru', reversed=True)  # Транслитерация с кириллицы на латиницу
        bot.reply_to(message, f"Транслитерированный текст: {transliterated_text}")
    else:
        bot.reply_to(message, "Пожалуйста, введите текст для транслитерации после команды /trans.")

# Запуск бота
bot.polling()
