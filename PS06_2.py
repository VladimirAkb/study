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

with open("divans.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Наименование товара', 'Цена', 'Ссылка на карточку'])
    writer.writerows(parsed_data)