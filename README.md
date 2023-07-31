# python-tic-tac-toe
### This is Homework Exercise 1 and 2 for CMPG 323

# Homework Exercise 1:
## Brief Description Of The Problem That My Code Solves
Tic Tac Toe is a classic two-player board game played on a 3x3 grid. The objective of the game is to be the first player to get three of their symbols (either 'X' or 'O') in a row, column, or diagonal. If all cells on the board are filled without any player achieving the objective, the game ends in a draw.

The problem presented for the creation of this code is the design of a simplistic and interactive interface to allow two players to play on the same device instead of using paper, and allow the users to play as many times as they like.
Although seemingly simplistic and irrelevant to many major coding projects, I think that the tic-tac-toe code has taught me a lot in terms of working with laying out a clean GUI, working with algorithms, event-handling, debugging and how to use various data structures as well as developing the thinking processes to try convert real-life scenarios into code by using OOP.

## My Problem-Solving Approach
Usually when approaching GUI problems I do a rough sketch of what I want the GUI to look like. In this case I made a simplistic sketch of a typical 3x3 grid used to play tic-tac-toe in a window. I also will begin to list the various functionalities of what the program must do. For example:
- allow a player to draw an X or a O inside a block on the grid
- everytime a symbol is drawn the program must check if the game is still in play (i.e, no one has won, lost or the board is not full)
- if the game is still in play, then the next user should be able to play their turn by drawing the symbol assigned to them
- if the game is not in play, the program should either state the winner if there is one or that the board is full

After considering all these points, I will then think of the steps and components to begin making the solution. This involves deciding what components will be used in the GUI (Buttons, messageboxes etc), the data structures I might use (Strings to display the symbols and arrays for the grid), how the output will be presented (Messageboxes, in the console), etc.
Finally after doing all the considerations and planning, I will begin with the actual implementation. During the coding process I usually test my code multiple times to make sure that everything is working and to avoid major errors later on in the solution. If changes need to be made I make use of source and version control to ensure that I can always revert back to previous versions.
Once I have completed the code I will run more tests on the program to ensure that there are no errors or bugs that I am unaware of and perform the necessary fixes. And once everything is working as it should and satifies all the functionalities I had planned out, I close the project and mark it as complete.
