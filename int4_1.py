from openai import OpenAI

# Создаем клиента с API ключом и базовым URL
client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I",  # Здесь вставьте ваш реальный API ключ
    base_url="https://api.proxyapi.ru/openai/v1",
)

def chat_with_ai():
    messages = [{"role": "user", "content": "Привет, чем могу помочь?"}]  # Начальное сообщение
    print("Вы можете начать чат с нейросетью. Для завершения напишите 'exit'.\n")

    while True:

        # Отправляем запрос к нейросети
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages
        )

        # Получаем ответ от нейросети
        ai_reply = chat_completion.choices[0].message.content
        #ai_reply = chat_completion.choices[0].message['content']
        # Выводим ответ нейросети
        print(f"Нейросеть: {ai_reply}\n")

        # Получаем ввод от пользователя
        user_input = input("Вы: ")

        # Если пользователь введет 'exit', завершаем чат
        if user_input.lower() == "exit":
            print("Завершаю чат. До свидания!")
            break

        # Добавляем сообщение пользователя в список сообщений
        messages.append({"role": "user", "content": user_input})
        # Добавляем ответ нейросети в список сообщений
        messages.append({"role": "assistant", "content": "отвечай в стилистике средневекового колдуна"})

# Запускаем функцию чата
chat_with_ai()
