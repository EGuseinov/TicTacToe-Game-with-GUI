import tkinter as tk
from tkinter import messagebox
import time

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        
        self.root.iconbitmap("icon.ico")

        self.current_player = "X"
        self.x_score = 0
        self.o_score = 0
        self.start_time = time.time()
        self.timer_running = True

        
        self.root.geometry("550x600")
        self.root.resizable(False, False)  
        self.create_widgets()
        self.create_board()
        self.update_timer()

    def create_widgets(self):
        self.frame_top = tk.Frame(self.root)
        self.frame_top.pack(pady=10)

        self.label_info = tk.Label(self.frame_top, text="Player X's turn", font=('normal', 15))
        self.label_info.pack(side=tk.LEFT, padx=5)

        self.label_timer = tk.Label(self.frame_top, text="Timer: 0", font=('normal', 15))
        self.label_timer.pack(side=tk.LEFT, padx=5)

        self.label_score = tk.Label(self.frame_top, text=" X: 0, O: 0", font=('normal', 15))
        self.label_score.pack(side=tk.LEFT, padx=5)

        self.frame_board = tk.Frame(self.root)
        self.frame_board.pack(pady=10)

    def create_board(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.frame_board, text=" ", font=('normal', 40), width=5, height=2,
                                   command=lambda r=row, c=col: self.click(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                button.bind("<Enter>", lambda event, r=row, c=col: self.on_enter(event, r, c))
                button.bind("<Leave>", lambda event, r=row, c=col: self.on_leave(event, r, c))
                self.buttons[row][col] = button

    def click(self, row, col):
        if self.buttons[row][col]["text"] == " ":
            self.buttons[row][col]["text"] = self.current_player
            self.buttons[row][col]["fg"] = "red" if self.current_player == "X" else "blue"
            self.buttons[row][col]["bg"] = "white"
            if self.check_win():
                self.timer_running = False
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                if self.current_player == "X":
                    self.x_score += 1
                else:
                    self.o_score += 1
                self.reset_board()
            elif self.is_full():
                self.timer_running = False
                messagebox.showinfo("Tic-Tac-Toe", "The game is a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label_info.config(text=f"Player {self.current_player}'s turn")

    def on_enter(self, event, row, col):
        if self.buttons[row][col]["text"] == " ":
            self.buttons[row][col].config(bg="red" if self.current_player == "X" else "blue")

    def on_leave(self, event, row, col):
        if self.buttons[row][col]["text"] == " ":
            self.buttons[row][col].config(bg="SystemButtonFace")

    def check_win(self):
        for row in range(3):
            if self.buttons[row][0]["text"] == self.buttons[row][1]["text"] == self.buttons[row][2]["text"] != " ":
                return True
        for col in range(3):
            if self.buttons[0][col]["text"] == self.buttons[1][col]["text"] == self.buttons[2][col]["text"] != " ":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != " ":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != " ":
            return True
        return False

    def is_full(self):
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]["text"] == " ":
                    return False
        return True

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = " "
                self.buttons[row][col].config(bg="SystemButtonFace")
        self.current_player = "X"
        self.label_info.config(text="Player X's turn")
        self.label_score.config(text=f" X: {self.x_score}, O: {self.o_score}")
        self.start_time = time.time() 
        self.timer_running = True  

    def update_timer(self):
        if self.timer_running:
            elapsed_time = int(time.time() - self.start_time)
            self.label_timer.config(text=f"Timer: {elapsed_time}")
        self.root.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
