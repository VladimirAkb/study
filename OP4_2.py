import math

def square(side):
    perimeter = 4 * side  # Периметр квадрата
    area = side ** 2  # Площадь квадрата
    diagonal = math.sqrt(2) * side  # Диагональ квадрата (по теореме Пифагора)
    return perimeter, area, diagonal  # Возвращаем кортеж

# Пример использования функции
side_length = int(input("Введите длину стороны квадрата: "))
perimeter, area, diagonal = square(side_length)

print(f"Периметр: {perimeter}")
print(f"Площадь: {area}")
print(f"Диагональ: {diagonal:.2f}")
