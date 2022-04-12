from .base import*

"""
    TIC TAC TOE Procedure   
"""


def isWon():
    pass


def isFilled(board):
    for i in range(0, length(board)):
        for j in range(0, length(board[i])):
            if board[i][j] != '':
                pass


def tictactoe():
    # Initialize TicTacToe Board
    board = [['', ''], ['', ''], ['', '']]
    boardFilled = isFilled(board)
