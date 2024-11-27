def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 1
    previous_char = s[0]

    for i in range(1, len(s)):
        if s[i] == previous_char:
            count += 1
        else:
            compressed.append(previous_char + str(count))
            previous_char = s[i]
            count = 1

    compressed.append(previous_char + str(count))
    return ''.join(compressed)

# Пример использования
input_string = "aabcccccaaa"
compressed_string = compress_string(input_string)
print("Сжатая строка:", compressed_string)