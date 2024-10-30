def valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    for i in range(9):
        if board[i][col] == num:
            return False
    subgrid_row = (row//3)*3
    subgrid_col = (col//3)*3
    for i in range(3):
        for j in range(3):
            if board[subgrid_row+i][subgrid_col+j] == num:
                return False
            
    return True

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = '.'
    return False

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                return i,j
            
    return None

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i!=0:
            print("---------------------") 
        for j in range(9):
            if j%3 == 0 and j != 0:
                print("|", end="")
            print(board[i][j], end=" ")
        print()

def inp_sudoku():
    board=[]
    print("Enter your sudoku puzzle row by row, using '.' for empty cells.")
    for i in range(9):
        while True:
            row = input(f"Row {i+1}: ").strip()
            if len(row) == 9 and all(c.isdigit() or c == '.' for c in row):
                board.append([int(c) if c.isdigit() else '.' for c in row])
                break
            else:
                print("Invalid input. The row should have exactly 9 characters (digits or'.')")
    return board

sudoku_board = inp_sudoku()

if solve_sudoku(sudoku_board):
    print("Sudoku puzzle solved!")
    print_board(sudoku_board)
else:
    print("No solution exists for the given puzzle")
    