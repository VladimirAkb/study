def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

a = int(input("Number 1: "))
b = int(input("Number 2: "))

print(safe_divide(a, b))