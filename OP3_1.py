# Ввод трех различных чисел
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

# Инициализация переменной для наименьшего числа
if a < b and a < c:
    min_number = a
elif b < a and b < c:
    min_number = b
else:
    min_number = c

# Вывод наименьшего числа
print(f"Наименьшее число: {min_number}")
