import tkinter as tk
from tkinter import messagebox

# Initialize game variables
board = ['' for _ in range(9)]   # Game board (list of 9 cells)
current_player = 'X'

# Set up the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create buttons for each cell in the grid
buttons = []
for cell in range(9):
    button_widget = tk.Button(root, text='', width=10, height=3, font=('normal', 20),
                              command=lambda index=cell: on_button_click(index))
    button_widget.grid(row=cell // 3, column=cell % 3)
    buttons.append(button_widget)


# Function to check winning combinations
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != '':
            return board[a]   # Return the winner ('X' or 'O')

    return None


# Function to reset the game
def reset_game():
    global board, current_player
    board = ['' for _ in range(9)]
    current_player = 'X'
    for button in buttons:
        button.config(text='')


# Function to handle cliks on the board
def on_button_click(cell):
    global current_player
    if board[cell] == '':
        board[cell] = current_player
        buttons[cell].config(text=current_player)

        # Checking the winner
        winner = check_winner()
        if winner:
            messagebox.showinfo("Congratulations!", f"🎉 Player {winner} wins! 🎉", icon='info')
            reset_game()
        elif '' not in board:
            messagebox.showinfo("Game Over", "It's a draw! 😞", icon='info')
            reset_game()
        else:
            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'


# Run the Tkinter event loop
root.mainloop()

























