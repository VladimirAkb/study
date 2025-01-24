#Инициализация: Для начала игры пользователю предлагается ввести количество побед, которые необходимы для завершения игры. После этого начинают показываться кнопки для выбора хода.
#Выбор игрока: Игрок выбирает один из вариантов (Камень, Ножницы, Бумага), и бот случайным образом генерирует свой ход. Далее определяется победитель раунда, обновляются очки, и игра продолжается до достижения указанного числа побед.
#Процесс игры: Когда один из игроков (пользователь или бот) достигает установленного количества побед, игра заканчивается, и выводится сообщение о победителе.
#Перезапуск игры: После завершения игры игрок может начать новую.


import telebot
from telebot import types
import random

# Создаем бота с токеном
API_TOKEN = '7662314218:AAEWqpenz2BgVap2csEHbfmskeuVDH5X3WE'
bot = telebot.TeleBot(API_TOKEN)

# Переменные для хранения состояния игры
user_score = 0
bot_score = 0
win_count = 0
game_started = False

# Словарь с вариантами игры
choices = ['камень', 'ножницы', 'бумага']

# Функция для начала новой игры
def start_game(message):
    global user_score, bot_score, win_count, game_started
    game_started = True
    user_score = 0
    bot_score = 0

    # Запрашиваем количество побед
    bot.send_message(message.chat.id, "Введите количество побед для окончания игры:")
    bot.register_next_step_handler(message, set_win_count)

# Функция для установки числа побед
def set_win_count(message):
    global win_count
    try:
        win_count = int(message.text)
        if win_count <= 0:
            bot.send_message(message.chat.id, "Количество побед должно быть больше 0. Попробуйте снова.")
            bot.register_next_step_handler(message, set_win_count)
        else:
            bot.send_message(message.chat.id, f"Игра началась! Победа по {win_count} очкам.")
            show_choices(message)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите число.")
        bot.register_next_step_handler(message, set_win_count)

# Функция для отображения кнопок выбора
def show_choices(message):
    if game_started:
        markup = types.ReplyKeyboardMarkup(row_width=3)
        button1 = types.KeyboardButton('Камень')
        button2 = types.KeyboardButton('Ножницы')
        button3 = types.KeyboardButton('Бумага')
        markup.add(button1, button2, button3)

        bot.send_message(message.chat.id, "Выберите ваш ход:", reply_markup=markup)

# Функция для обработки выбора пользователя
@bot.message_handler(func=lambda message: message.text.lower() in choices)
def user_move(message):
    global user_score, bot_score, game_started
    if not game_started:
        bot.send_message(message.chat.id, "Игра еще не началась")
        return

    user_choice = message.text.lower()
    bot_choice = random.choice(choices)

    if user_choice == bot_choice:
        result = "Ничья!"
    elif (user_choice == 'камень' and bot_choice == 'ножницы') or \
         (user_choice == 'ножницы' and bot_choice == 'бумага') or \
         (user_choice == 'бумага' and bot_choice == 'камень'):
        user_score += 1
        result = f"Вы победили! Ваш ход: {user_choice}, ход бота: {bot_choice}."
    else:
        bot_score += 1
        result = f"Вы проиграли! Ваш ход: {user_choice}, ход бота: {bot_choice}."

    # Отправляем результат
    bot.send_message(message.chat.id, result)
    bot.send_message(message.chat.id, f"Счет: Вы {user_score} - Бот {bot_score}")

    # Проверяем, не достиг ли кто-то победы
    if user_score >= win_count:
        bot.send_message(message.chat.id, "Поздравляем, вы победили в игре!")
        game_started = False
    elif bot_score >= win_count:
        bot.send_message(message.chat.id, "Бот победил!")
        game_started = False
    else:
        show_choices(message)

# Функция, если пользователь введет текст, не относящийся к выбору
@bot.message_handler(func=lambda message: True)
def handle_other(message):
    if not game_started:
        start_game(message)

# Запуск бота
bot.polling(none_stop=True)

