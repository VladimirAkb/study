from arithmetic import *

while True:
    user_input = input("Пожалуйста, введите первое число: ")
    try:
        num1 = float(user_input)
        break  # Выход из цикла, если преобразование прошло успешно
    except ValueError:
        print("Невозможно преобразовать введенное значение в целое число. Пожалуйста, попробуйте еще раз.")

while True:
    user_input = input("Пожалуйста, введите второе число: ")
    try:
        num2 = float(user_input)
        break  # Выход из цикла, если преобразование прошло успешно
    except ValueError:
        print("Невозможно преобразовать введенное значение в целое число. Пожалуйста, попробуйте еще раз.")

print("Результат сложения: " + str(summa(num1, num2)))
print("Результат вычитания: " + str(razn(num1, num2)))
print("Результат умнрожения: " + str(umn(num1, num2)))
print("Результат деления: " + str(delen(num1, num2)))
