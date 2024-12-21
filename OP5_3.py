#Задание 2 из урока OP3
#Простой калькулятор, который выполняет одну из операций (+, -, *, /) над двумя введенными пользователем числами

# Ввод первого числа
while True:
    num1 = input("Введите первое число: ")
    try:
        num1 = float(num1)
        break
    except:
        print("Неверное значение! Попробуйте еще раз")

# Ввод второго числа
while True:
    num2 = input("Введите второе число: ")
    try:
        num2 = float(num2)
        break
    except:
        print("Неверное значение! Попробуйте еще раз")


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
    try:
        result = num1 / num2
    except ZeroDivisionError:
        result = "Ошибка! Деление на ноль."
    except:
        result = "Ошибка! Неверная операция."
else:
    result = "Ошибка! Неверная операция."

# Вывод результата
print(f"Результат: {result}")
