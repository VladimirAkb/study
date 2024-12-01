# Ввод номера месяца
month = int(input("Введите номер месяца (1-12): "))

# Определение количества дней в месяце с использованием условных операторов
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
elif month == 2:
    days = 28  # Для невисокосного года февраль имеет 28 дней
else:
    days = "Ошибка! Неверный номер месяца."

# Вывод результата
print(f"Количество дней в месяце: {days}")
