import random

list_all = ["Alex", "Bob", "Phil", "Pam", "Tom", "Sam", "Din", "Alex"]
list_sel = []

print(list_all)

while True:
    el = random.choice(list_all)
    print(el)
    if list_sel.count(el) == 0:
        list_sel.append(el)
    if len(list_sel) >= 5:
        break

print(list_sel)