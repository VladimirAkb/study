# Ввод начала и конца диапазона
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

# Перебор чисел в диапазоне с использованием цикла for
print("Четные числа в диапазоне:")
for num in range(start, end + 1):
    if num % 2 == 0:  # Проверка на четность
        print(num)
