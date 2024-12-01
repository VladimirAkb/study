# Ввод двух чисел
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Ввод операции
operation = input("Введите операцию (+, -, *, /): ")

# Выполнение соответствующей операции с использованием условных операторов
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Ошибка! Деление на ноль."
else:
    result = "Ошибка! Неверная операция."

# Вывод результата
print(f"Результат: {result}")
