# PRODIGY_SD_04

## Sudoku Solver

This Python program solves a 9x9 Sudoku puzzle. It allows the user to input an unsolved Sudoku grid, where empty cells are represented by dots ('.'). The program uses a backtracking algorithm to attempt to solve the puzzle. It checks the validity of placing a number in each cell by ensuring that the number doesn't already exist in the same row, column, or 3x3 subgrid. If a number fits, it moves to the next empty cell. If no valid number can be placed, it backtracks to the previous cell to try a different number. 
Once the puzzle is solved, the completed board is printed. If no solution exists, the program notifies the user.
