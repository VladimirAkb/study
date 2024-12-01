#import openai

## Настройка API
#openai.api_key = "sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I"  # Замените на ваш реальный API ключ
#openai.api_base = "https://api.proxyapi.ru/openai/v1"  # Базовый URL для вашего прокси API

from openai import OpenAI


client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I",
    base_url="https://api.proxyapi.ru/openai/v1",
)

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106", messages=[{"role": "user", "content": "Hello world"}]
)

def chat_with_ai():
    # Начальное сообщение для начала чата
    messages = [{"role": "user", "content": "Привет, чем могу помочь?"}]
    print("Вы можете начать чат с нейросетью. Для завершения напишите 'exit'.\n")

    while True:
        # Получаем ввод от пользователя
        user_input = input("Вы: ")

        # Если пользователь введет 'exit', завершаем чат
        if user_input.lower() == "exit":
            print("Завершаю чат. До свидания!")
            break

        # Добавляем сообщение пользователя в список сообщений
        messages.append({"role": "user", "content": user_input})

        try:
            # Отправляем запрос к нейросети
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-1106",
                messages=messages
            )

            # Получаем ответ от нейросети
            ai_reply = response['choices'][0]['message']['content']

            # Выводим ответ нейросети
            print(f"Нейросеть: {ai_reply}\n")

            # Добавляем ответ нейросети в список сообщений
            messages.append({"role": "assistant", "content": ai_reply})


        except Exception as e:

            print(f"Ошибка при запросе к API: {e}")


# Запускаем функцию чата

chat_with_ai()