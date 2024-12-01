def bank(a, years):
    # Изначальная сумма вклада
    total = a
    # Проходим по каждому году и увеличиваем сумму на 10%
    for year in range(years):
        total += total * 0.1  # Прибавляем 10% от текущей суммы
    return total

# Пример использования функции
a = float(input("Введите сумму вклада (в рублях): "))
years = int(input("Введите срок вклада (в годах): "))

final_amount = bank(a, years)
print(f"Сумма на счету через {years} лет: {final_amount:.2f} рублей")
