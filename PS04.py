from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def open_wikipedia_article(query, browser):
    browser.get("https://ru.wikipedia.org")
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

def list_paragraphs(browser):
    paragraphs = browser.find_elements(By.CSS_SELECTOR, "div.mw-parser-output > p")
    for i, p in enumerate(paragraphs):
        text = p.text.strip()
        if text:
            print(f"\n[{i + 1}] {text}")
            input("Нажмите Enter для продолжения или Ctrl+C для выхода из чтения...")

def get_internal_links(browser):
    links = browser.find_elements(By.CSS_SELECTOR, "div.mw-parser-output a[href^='/wiki/']")
    filtered_links = [link for link in links if ':' not in link.get_attribute('href')]  # Убираем служебные ссылки
    seen = set()
    unique_links = []
    for link in filtered_links:
        href = link.get_attribute('href')
        text = link.text.strip()
        if text and href not in seen:
            seen.add(href)
            unique_links.append((text, href))
        if len(unique_links) >= 5:
            break
    return unique_links

def main():
    browser = webdriver.Chrome()
    try:
        query = input("Введите запрос для поиска в Википедии: ")
        open_wikipedia_article(query, browser)

        while True:
            print("\nЧто вы хотите сделать?")
            print("1. Читать параграфы текущей статьи")
            print("2. Перейти на связанную статью")
            print("3. Выйти из программы")
            choice = input("Введите номер действия (1-3): ")

            if choice == '1':
                list_paragraphs(browser)

            elif choice == '2':
                links = get_internal_links(browser)
                if not links:
                    print("Связанных статей не найдено.")
                    continue
                print("\nСвязанные статьи:")
                for i, (text, _) in enumerate(links, start=1):
                    print(f"{i}. {text}")
                link_choice = input("Введите номер статьи для перехода (или Enter для отмены): ")
                if link_choice.isdigit():
                    link_idx = int(link_choice) - 1
                    if 0 <= link_idx < len(links):
                        browser.get(links[link_idx][1])
                        time.sleep(2)
                    else:
                        print("Неверный номер.")
                else:
                    print("Отмена перехода.")

            elif choice == '3':
                print("Выход из программы.")
                break
            else:
                print("Некорректный ввод. Попробуйте снова.")
    finally:
        browser.quit()

if __name__ == "__main__":
    main()
