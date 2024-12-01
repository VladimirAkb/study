def sum_range(start, end):
    summ = 0
    if start > end:
        print("Неверные аргументы!")
        return summ

    for i in range(start,end+1):
        summ += i
    return summ


start = int(input("Введите начальное число: "))
end = int(input("Введите конечное число: "))
print("Сумма чисел от " + str(start) + " до " + str(end) + " равна: " + str(sum_range(start, end)))
