import pandas as pd
import matplotlib.pyplot as plt
import time
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.divan.ru/category/svet"

driver.get(url)
time.sleep(3)

lights = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')
print(len(lights))

parsed_data = []

for light in lights:
    title = ''
    link = ''
    price = 0
    try:
        title = light.find_element(By.CSS_SELECTOR, 'a.ProductName span[itemprop="name"]').text.strip()
        title_element = light.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8')
        link = title_element.get_attribute('href')
        price_tag = light.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]')
        price = price_tag.get_attribute('content')
        parsed_data.append([title, price, link])
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

driver.quit()

with open("for_hist.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Наименование товара', 'Цена', 'Ссылка на карточку'])
    writer.writerows(parsed_data)


# 1. Загрузка данных из файла for_hist.csv
df = pd.read_csv('for_hist.csv')

# Проверим, что данные загружены корректно
print("Первые 5 строк датафрейма:")
print(df.head())

# Убедимся, что колонка 'Цена' имеет числовой формат (если нужно — преобразуем)
df['Цена'] = pd.to_numeric(df['Цена'], errors='coerce')

# 2. Вывод среднего значения по колонке 'Цена'
average_price = df['Цена'].mean()
print(f"\nСреднее значение цены: {average_price:.2f}")

# 3. Построение гистограммы по ценам
plt.figure(figsize=(10, 6))
plt.hist(df['Цена'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Гистограмма цен товаров')
plt.xlabel('Цена')
plt.ylabel('Количество товаров')
plt.grid(True)
plt.tight_layout()
plt.show()