import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Крестики-нолики")
        self.window.geometry("320x450")
        self.window.configure(bg="#F0F0F0")

        self.player_choice = None
        self.current_player = "X"
        self.scores = {"X": 0, "O": 0}
        self.win_goal = 3  # Количество побед для завершения матча
        self.buttons = []

        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        tk.Label(self.window, text="Выберите X или O:", font=("Arial", 12), bg="#F0F0F0").pack()

        choice_frame = tk.Frame(self.window, bg="#F0F0F0")
        choice_frame.pack()

        tk.Button(choice_frame, text="X", font=("Arial", 12), width=5, command=lambda: self.set_player("X")).pack(
            side=tk.LEFT, padx=10)
        tk.Button(choice_frame, text="O", font=("Arial", 12), width=5, command=lambda: self.set_player("O")).pack(
            side=tk.LEFT, padx=10)

        tk.Label(self.window, text="До скольки побед играем?", font=("Arial", 12), bg="#F0F0F0").pack(pady=5)

        self.win_goal_var = tk.StringVar(value="3")
        win_frame = tk.Frame(self.window, bg="#F0F0F0")
        win_frame.pack()

        for num in [3, 5, 7]:
            tk.Button(win_frame, text=str(num), font=("Arial", 12), width=5,
                      command=lambda n=num: self.set_win_goal(n)).pack(side=tk.LEFT, padx=5)

        self.score_label = tk.Label(self.window, text="Счет: X - 0 | O - 0", font=("Arial", 12), bg="#F0F0F0")
        self.score_label.pack(pady=5)

        self.board_frame = tk.Frame(self.window, bg="#F0F0F0")
        self.board_frame.pack()

        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(self.board_frame, text="", font=("Arial", 20), width=5, height=2, bg="white",
                                command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

        self.reset_button = tk.Button(self.window, text="Сброс", font=("Arial", 10), width=10, command=self.reset_game)
        self.reset_button.pack(pady=5)

    def set_player(self, choice):
        self.player_choice = choice
        self.current_player = choice
        messagebox.showinfo("Игра начинается!", f"Вы играете за {choice}!")

    def set_win_goal(self, goal):
        self.win_goal = goal
        messagebox.showinfo("Цель установлена", f"Игра идет до {goal} побед!")

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return self.buttons[i][0]["text"]
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return self.buttons[0][i]["text"]

        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return self.buttons[0][0]["text"]
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return self.buttons[0][2]["text"]

        return None

    def check_draw(self):
        return all(self.buttons[i][j]["text"] != "" for i in range(3) for j in range(3))

    def on_click(self, row, col):
        if not self.player_choice:
            messagebox.showwarning("Выбор игрока", "Сначала выберите X или O!")
            return

        if self.buttons[row][col]["text"] != "":
            return

        self.buttons[row][col]["text"] = self.current_player

        winner = self.check_winner()
        if winner:
            self.scores[winner] += 1
            messagebox.showinfo("Победа!", f"Игрок {winner} победил!")
            self.update_score()
            if self.scores[winner] >= self.win_goal:
                messagebox.showinfo("Конец матча", f"Игрок {winner} выиграл матч!")
                self.reset_game(full_reset=True)
            else:
                self.reset_board()
            return

        if self.check_draw():
            messagebox.showinfo("Ничья!", "Ничья! Начнем заново.")
            self.reset_board()
            return

        self.current_player = "O" if self.current_player == "X" else "X"

    def update_score(self):
        self.score_label.config(text=f"Счет: X - {self.scores['X']} | O - {self.scores['O']}")

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""

    def reset_game(self, full_reset=False):
        if full_reset:
            self.scores = {"X": 0, "O": 0}
            self.player_choice = None
            self.win_goal = 3  # Возвращаем стандартное значение
            self.score_label.config(text="Счет: X - 0 | O - 0")
        self.reset_board()


TicTacToe()
