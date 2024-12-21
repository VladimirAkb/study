import tkinter as tk
from tkinter import Button

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

def mark_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.itemconfig(selected_task, bg="AntiqueWhite4")


root = tk.Tk()
root.title("ToDo List")
root.configure(background="AntiqueWhite1")

text_lbl1 = tk.Label(root, background="AntiqueWhite1", text="Введите вашу задачу:")
text_lbl1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="AntiqueWhite3",border=3)
task_entry.pack(pady=10)

new_task = tk.Button(root, bg = "AntiqueWhite3", width=20, text = "Добавить задачу", command=add_task)
new_task.pack(pady = 5)

del_task = tk.Button(root, bg = "AntiqueWhite3", width=20, text = "Удалить задачу", command=delete_task)
del_task.pack(pady = 5)

mrk_task = tk.Button(root, bg = "AntiqueWhite3", width=20, text = "Отметить задачу", command=mark_task)
mrk_task.pack(pady = 5)

text_lbl2 = tk.Label(root, background="AntiqueWhite1", text="Список задач:")
text_lbl2.pack(pady=5)

task_list = tk.Listbox(root, height=10, width=50, bg="AntiqueWhite3")
task_list.pack(pady=10)

root.mainloop()