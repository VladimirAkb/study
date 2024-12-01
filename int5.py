import telebot
#import openai
from openai import OpenAI
from transliterate import translit

# Замените на ваш реальный токен
API_TOKEN = '7662314218:AAEWqpenz2BgVap2csEHbfmskeuVDH5X3WE'
OPENAI_API_KEY = 'sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I'  # Замените на ваш OpenAI API ключ

# Инициализация бота и OpenAI
bot = telebot.TeleBot(API_TOKEN)
#openai.api_key = OPENAI_API_KEY
# Создаем клиента с API ключом и базовым URL
client = OpenAI(
    api_key=OPENAI_API_KEY,  # Здесь вставьте ваш реальный API ключ
    base_url="https://api.proxyapi.ru/openai/v1",
)
# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram-бот. Напиши мне что-нибудь, и я постараюсь ответить.")

# Команда /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Я могу отвечать на твои вопросы, используя нейросеть. Напиши мне любое сообщение, и я постараюсь помочь.")

# Команда /trans для транслитерации
@bot.message_handler(commands=['trans'])
def transliterate_text(message):
    text = message.text[7:]  # Убираем команду '/trans ' из текста
    if text:
        transliterated_text = translit(text, 'ru', reversed=True)  # Транслитерация с кириллицы на латиницу
        bot.reply_to(message, f"Транслитерированный текст: {transliterated_text}")
    else:
        bot.reply_to(message, "Пожалуйста, введите текст для транслитерации после команды /trans.")

# Функция для общения с нейросетью (например, GPT)
def get_ai_response(user_message):
    try:
        messages = [{"role": "user", "content": user_message}]  # Начальное сообщение
        # Отправляем запрос к нейросети
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages
        )

        # Получаем ответ от нейросети
        ai_reply = chat_completion.choices[0].message.content
        return ai_reply

        #response = openai.ChatCompletion.create(
        #    model="gpt-3.5-turbo-1106",  # Вы можете использовать любую модель из доступных
        #    messages=[{"role": "user", "content": user_message}]
        #)
        #return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Произошла ошибка при запросе к нейросети: {str(e)}"

# Обработка всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def respond_to_message(message):
    user_message = message.text
    ai_response = get_ai_response(user_message)
    bot.reply_to(message, ai_response)

# Запуск бота
bot.polling()
