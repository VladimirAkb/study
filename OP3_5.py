import random

# Функция для получения выбора игрока
def get_player_choice():
    choice = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()
    while choice not in ["камень", "ножницы", "бумага"]:
        print("Неверный выбор! Пожалуйста, выберите камень, ножницы или бумагу.")
        choice = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()
    return choice


# Функция для получения случайного выбора компьютера
def get_computer_choice():
    return random.choice(["камень", "ножницы", "бумага"])

# Функция для определения победителя в раунде
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "ничья"
    elif (player_choice == "камень" and computer_choice == "ножницы") or \
            (player_choice == "ножницы" and computer_choice == "бумага") or \
            (player_choice == "бумага" and computer_choice == "камень"):
        return "игрок"
    else:
        return "компьютер"


# Основная программа
player_wins = 0
computer_wins = 0

while player_wins < 3 and computer_wins < 3:
    print(f"\nСчёт: Игрок - {player_wins}, Компьютер - {computer_wins}")

    # Получаем выбор игрока и компьютера
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    # Показываем выборы
    print(f"Вы выбрали: {player_choice}")
    print(f"Компьютер выбрал: {computer_choice}")

    # Определяем победителя раунда
    round_winner = determine_winner(player_choice, computer_choice)

    if round_winner == "игрок":
        player_wins += 1
        print("Вы победили в этом раунде!")
    elif round_winner == "компьютер":
        computer_wins += 1
        print("Компьютер победил в этом раунде!")
    else:
        print("Ничья в этом раунде!")

# Определяем окончательного победителя
if player_wins == 3:
    print("\nПоздравляем! Вы выиграли игру!")
else:
    print("\nКомпьютер выиграл игру!")
