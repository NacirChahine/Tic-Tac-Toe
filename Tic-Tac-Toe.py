import tkinter as tk
from tkinter import messagebox

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    if "" not in sum(board, []):
        return "Draw"
    return None

def on_click(row, col):
    global current_player

    if board[row][col] == "" and current_player == "X":
        buttons[row][col].config(text="X", state="disabled")
        board[row][col] = "X"
        current_player = "O"
    elif board[row][col] == "" and current_player == "O":
        buttons[row][col].config(text="O", state="disabled")
        board[row][col] = "O"
        current_player = "X"

    winner = check_winner()
    if winner:
        if winner == "Draw":
            messagebox.showinfo("XO by Nacir", "It's a draw!")
        else:
            messagebox.showinfo("XO by Nacir", f"{winner} wins!")
        root.quit()

# Initialize the board
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"

# Create the main window
root = tk.Tk()
root.title("XO by Nacir")

# Create buttons for the board
buttons = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Helvetica", 20), width=5, height=2,
                                  command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
