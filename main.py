import random

# Ввод диапазона
lower_bound = int(input("Введите нижнюю границу диапазона: "))
upper_bound = int(input("Введите верхнюю границу диапазона: "))

# Генерация случайного числа в заданном диапазоне
random_number = random.randint(lower_bound, upper_bound)

# Вывод случайного числа
print(f"Случайное число в диапазоне от {lower_bound} до {upper_bound}: {random_number}")
