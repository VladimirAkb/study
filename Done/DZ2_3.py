def caesar_cipher(text, shift, decrypt=False):
    # Если необходимо дешифрование, инвертируем сдвиг
    if decrypt:
        shift = -shift

    result = []

    for char in text:
        if char.isalpha():
            # Определяем базу (начальный код) для заглавных и строчных букв
            base = ord('A') if char.isupper() else ord('a')
            # Находим смещенный символ
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)
        else:
            # Если символ не является буквой, добавляем его без изменений
            result.append(char)

    return ''.join(result)


# Пример использования
original_text = "Hello, World!"
shift = 3

# Шифрование
encrypted_text = caesar_cipher(original_text, shift)
print("Зашифрованный текст:", encrypted_text)

# Дешифрование
decrypted_text = caesar_cipher(encrypted_text, shift, decrypt=True)
print("Расшифрованный текст:", decrypted_text)