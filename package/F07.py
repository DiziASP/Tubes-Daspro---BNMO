from .base import*

"""
    Game's List Procedure   
"""


def list_game_toko(game):
    sorter = input(
        """
    tahun+ || tahun- 
    harga+ || harga-
    Masukkan Skema Pencarian:
    """)
    if length(sorter) == 0:
        idx = 0
        res = removeFirstElmt(game)
        res = sortMatrix(res, idx, '+')
        printGame(res, 1)
    elif (sorter == 'tahun+'):
        idx = 3
        res = removeFirstElmt(game)
        res = sortMatrix(res, idx, '+')
        printGame(res, 1)
    elif (sorter == 'tahun-'):
        idx = 3
        res = removeFirstElmt(game)
        res = sortMatrix(res, idx, '-')
        printGame(res, 1)
    elif (sorter == 'harga+'):
        idx = 4
        res = removeFirstElmt(game)
        res = sortMatrix(res, idx, '+')
        printGame(res, 1)
    elif (sorter == 'harga-'):
        idx = 4
        res = removeFirstElmt(game)
        res = sortMatrix(res, idx, '-')
        printGame(res, 1)
    else:
        input("Skema sorting tidak valid")
    input("Press any key to continue...")
    return
