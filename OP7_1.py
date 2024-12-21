import tkinter as tk

def hello_click():
    namestr = "Привет, " + name.get()
    hello.config(text=namestr)

root = tk.Tk()

root.title("Задание по модулю 7:")
label = tk.Label(root, text = "Введите имя: ")
label.pack()

name = tk.Entry(root)
name.pack()

hello = tk.Label(root, text="")

create_hello = tk.Button(root, text="ВВОД", command=hello_click)
create_hello.pack()

hello.pack()

root.mainloop()
