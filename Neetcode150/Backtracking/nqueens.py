global n
n = 4


def display(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def is_safe(board, row, col):
    # check for up _> row--, col -> i = row (til i >= 0)
    for i in range(row, 0, -1):
        if board[i][col] == 1:  # queen already present
            return False  # can't be placed

    # check for up right -> row--. col++ (i = row, j = col, til i >= 0 and j <= len(board))
    for i, j in zip(range(row, 0, -1), range(col, len(board[0]), 1)):
        if board[i][j] == 1:
            return False

    # check for up left -> row--, col (i >+ 0 and j >= 0
    for i, j in zip(range(row, 0, -1), range(col, 0, -1)):
        if board[i][j] == 1:
            return False

    # else can be placed
    return True


def nqueen(board, row):
    # base case
    if row == len(board):
        display(board)
        return

    # recursive
    for i in range(n):
        if is_safe(board, i, col):
            # place
            board[row][col] = 1
            nqueen(board, row + 1)
            board[row][col] = 0  # backtrack
    # if cant be placed
    return False


def main():
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    if nqueen(board, 0) == False:
        print("no soln")
        return False
    display(board)
    return True


main()
