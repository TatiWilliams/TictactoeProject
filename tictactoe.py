board = [" ", "0", "1", "2",
         "0", "_", "_", "_",
         "1", "_", "_", "_",
         "2", "_", "_", "_"]

currentPlayer = "X"
winner = None
game_running = True


def printBoard(board):
    print(board[0] + " " + board[1] + " " + board[2] + " " + board[3])
    print(board[4] + " " + board[5] + " " + board[6] + " " + board[7])
    print(board[8] + " " + board[9] + " " + board[10] + " " + board[11])
    print(board[12] + " " + board[13] + " " + board[14] + " " + board[15])


def playerInput(board):
    row = int(input("Введи номер строки (0, 1, 2): "))
    col = int(input("Введи номер столбца (0, 1, 2): "))
    position = (row + 1) * 4 + col + 1
    if board[position] == "_":
        board[position] = currentPlayer
    else:
        print("Это место занято!")
        playerInput(board)


def checkHorizontal(board):
    global winner
    if board[5] == board[6] == board[7] and board[5] != "_":
        winner = board[5]
        return True
    elif board[9] == board[10] == board[11] and board[9] != "_":
        winner = board[9]
        return True
    elif board[13] == board[14] == board[15] and board[13] != "_":
        winner = board[13]
        return True


def checkVertical(board):
    global winner
    if board[5] == board[9] == board[13] and board[5] != "_":
        winner = board[5]
        return True
    elif board[6] == board[10] == board[14] and board[6] != "_":
        winner = board[6]
        return True
    elif board[7] == board[11] == board[15] and board[7] != "_":
        winner = board[7]
        return True


def checkDiagonal(board):
    global winner
    if board[5] == board[10] == board[15] and board[5] != "_":
        winner = board[5]
        return True
    elif board[13] == board[10] == board[7] and board[13] != "_":
        winner = board[13]
        return True


def checkTie(board):
    global game_running
    if "_" not in board:
        printBoard(board)
        print("Это ничья!")
        game_running = False


def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        printBoard(board)
        print(f"Победил  {winner}")


def switchPlayer():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"


while game_running:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
