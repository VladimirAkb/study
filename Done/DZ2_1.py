def count_numbers_with_digit_3(start, end):
    count = 0
    for number in range(start, end + 1):
        if '3' in str(number):
            count += 1
    return count

# Задаем диапазон от 1 до 2024
start = 1
end = 2024

# Вычисляем количество чисел с цифрой 3
result = count_numbers_with_digit_3(start, end)
print("Количество чисел от 1 до 2024, содержащих хотя бы одну цифру 3:", result)