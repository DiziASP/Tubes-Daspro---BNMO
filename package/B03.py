from .base import*

"""
    TIC TAC TOE Procedure   
"""


def filled(board: list) -> bool:
    for i in range(0, length(board)):
        for j in range(0, length(board[i])):
            if board[i][j] != "":
                return False
    return True


def checkboard(board: list, X: int, Y: int, turn: str) -> bool:
    if board[X][Y] == "X" and turn == "O":
        print("Kolomnya udah ada yang punya mas/mbak e :(")
        return False
    elif board[X][Y] == "O" and turn == "X":
        print("Kolomnya udah ada yang punya mas/mbak e :(")
        return False
    elif board[X][Y] != " ":
        print("Kolomnya udah ada di isi mas/mbak e :(")
        return False
    else:
        return True


def check(board: list, player: chr) -> bool:
    if filled(board):
        print("It's a tieeeeeeee!!!!!!")
        return True
    if (board[0][0] == board[0][1] == board[0][2] == 'X') or (board[0][0] == board[0][1] == board[0][2] == 'O'):  # Atas Mendatar
        print(f"Player {player} Wins.")
        return True
    elif (board[1][0] == board[1][1] == board[1][2] == 'X') or (board[1][0] == board[1][1] == board[1][2] == 'O'):  # Tengah Mendatar
        print(f"Player {player} Wins.")
        return True
    elif (board[2][0] == board[2][1] == board[2][2] == 'X') or (board[2][0] == board[2][1] == board[2][2] == 'O'):  # Bawah Mendatar
        print(f"Player {player} Wins.")
        return True
    elif (board[0][0] == board[1][0] == board[2][0] == 'X') or (board[0][0] == board[1][0] == board[2][0] == 'O'):  # Kiri Vertikal
        print(f"Player {player} Wins.")
        return True
    elif (board[0][1] == board[1][1] == board[2][1] == 'X') or (board[0][1] == board[1][1] == board[2][1] == 'O'):  # Tengah Vertikal
        print(f"Player {player} Wins.")
        return True
    elif (board[0][2] == board[1][2] == board[2][2] == 'X') or (board[0][2] == board[1][2] == board[2][2] == 'O'):  # Tengah Vertikal
        print(f"Player {player} Wins.")
        return True
    elif (board[0][0] == board[1][1] == board[2][2] == 'X') or (board[0][0] == board[1][1] == board[2][2] == 'O'):  # Diagonal
        print(f"Player {player} Wins.")
        return True
    elif (board[2][0] == board[1][1] == board[0][2] == 'X') or (board[2][0] == board[1][1] == board[0][2] == 'O'):  # Diagonal
        print(f"Player {player} Wins.")
        return True
    else:
        return False


def printBoard(board: list):
    print("1 2 3")
    for i in range(0, length(board)):
        for j in range(0, length(board[i])):
            if j == 2:
                print(board[i][j])
            else:
                print(board[i][j], end="|")
        print("-+-+-")


def modBoard(board: list, X: int, Y: int, turn: chr):
    board[X][Y] = turn
    return board


def tictactoe():
    # Initialize TicTacToe Board
    turn = 'X'
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    won = False
    while won != True:
        os.system("cls")
        print(f"Player {turn} turn!")
        printBoard(board)
        while True:
            try:
                X = int(input('X-Axis: '))-1
                Y = int(input('Y-Axis: '))-1
                if (X < 0 or X > 2) or (Y < 0 or Y > 2):
                    print("Inputnya yang benar ya sayang ya")
                    continue
                if checkboard(board, X, Y, turn) == False:
                    continue
                else:
                    break
            except ValueError:
                print("Inputnya yang benar ya sayang ya")
                continue

        board = modBoard(board, X, Y, turn)
        printBoard(board)
        won = check(board, turn)  # Check if there is a winner
        if turn == 'X':
            turn = 'O'
        elif turn == 'O':
            turn = 'X'
        if won == True:
            break
        input("Lanjut...")
