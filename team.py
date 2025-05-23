import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x350")

current_player = "X"
buttons = []


def check_winner():
   for i in range(3):
       if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
           return True
       if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
           return True

   if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
       return True
   if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
       return True

   return False

def check_draw():
   for i in range(3):
       for ii in range(3):
           if buttons[i][ii]["text"] == "":
               return False

   return True

def reset_game():
   current_player = "X"
   for i in range(3):
       for ii in range(3):
           buttons[i][ii]['text'] = ""


def on_click(row, col):
   global current_player

   if buttons[row][col]['text'] != "":
       return

   buttons[row][col]['text'] = current_player

   if check_winner():
       messagebox.showinfo("Игра окончена",f"Игрок {current_player} победил!")

   if check_draw():
       messagebox.showinfo("Игра окончена", "Ничья!")

   current_player = "0" if current_player == "X" else "X"

for i in range(3):
   row = []
   for j in range(3):
       btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
       btn.grid(row=i, column=j)
       row.append(btn)
   buttons.append(row)

btn_clear = tk.Button(window, text = "Сброс", font=("Arial", 8), width=5, height=2, command=reset_game)
btn_clear.grid(row=3,column=0)

window.mainloop()

