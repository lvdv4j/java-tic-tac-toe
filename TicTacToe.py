import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        # Initialize the TicTacToe class with the main root window
        self.root = root
        self.root.title("Tic Tac Toe")

        # Set the initial player to 'X'
        self.current_player = 'X'
        self.root.title("Tic Tac Toe: Player X's Turn")
        root.resizable(width=False, height=False)

        # Create a 3x3 game board using a list of lists
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        # Create a 3x3 grid of buttons using a list of lists
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                # Increase the font size and adjust the button size
                self.buttons[i][j] = tk.Button(root, text=' ', font=('Helvetica', 25),
                                               width=8, height=4, command=lambda row=i, col=j: self.on_click(row, col))
                # Position the button on the grid
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        # Check if the selected cell on the board is empty
        if self.board[row][col] == ' ':
            # Set the current player's symbol on the board
            self.board[row][col] = self.current_player
            # Update the button text to display the current player's symbol
            self.buttons[row][col].config(text=self.current_player)
            # Check if the current player has won the game
            if self.check_winner(row, col):
                self.show_winner()
            # Check if the game is a draw (no empty cells left)
            elif self.check_draw():
                self.show_draw()
            else:
                # Switch the player for the next move
                self.switch_player()
                self.root.title("Tic Tac Toe: Player " +self.current_player + "'s Turn")

    def switch_player(self):
        # Switch the current player between 'X' and 'O'
        self.current_player = 'X' if self.current_player == 'O' else 'O'

    def check_winner(self, row, col):
        # Get the symbol of the current player at the selected cell
        player = self.board[row][col]
        # Check if the player has won the game by checking rows, columns, and diagonals
        return (
            all(self.board[row][c] == player for c in range(3)) or
            all(self.board[r][col] == player for r in range(3)) or
            all(self.board[i][i] == player for i in range(3)) or
            all(self.board[i][2-i] == player for i in range(3))
        )

    def check_draw(self):
        # Check if all cells on the board are filled (no empty cells)
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def show_winner(self):
        # Show a message box with the winner's symbol ('X' or 'O')
        winner = 'Player X' if self.current_player == 'X' else 'Player O'
        messagebox.showinfo("Game Over", f"{winner} wins!")
        # Reset the game after displaying the winner
        self.reset_game()

    def show_draw(self):
        # Show a message box indicating the game is a draw
        messagebox.showinfo("Game Over", "It's a draw!")
        # Reset the game after displaying the draw message
        self.reset_game()

    def reset_game(self):
        # Reset the game by setting the current player to 'X'
        # and clearing the game board
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        # Clear the button text on the GUI
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ')

if __name__ == "__main__":
    # Create the main root window
    root = tk.Tk()
    # Initialize the TicTacToe class with the main root window
    tictactoe = TicTacToe(root)
    # Start the GUI main event loop
    root.mainloop()
