from .base import*

"""
    Game's List Procedure   
"""


def list_game_toko(game):
    sorter = strip_str(input(  # Input sorting method
        """
    tahun+ || tahun- 
    harga+ || harga-
    Masukkan Skema Pencarian:
    """))

    if length(sorter) == 0:  # If there is no chosen sorter method
        idx = 0
        res = removeFirstElmt(game)
        res = sortMatrix(res, idx, '+')
        printGame(res, 1)
    elif (sorter == 'tahun+'):  # Ascending year
        idx = 3
        res = removeFirstElmt(game)
        res = sortMatrix(res, idx, '+')
        printGame(res, 1)
    elif (sorter == 'tahun-'):  # Descending year
        idx = 3
        res = removeFirstElmt(game)
        res = sortMatrix(res, idx, '-')
        printGame(res, 1)
    elif (sorter == 'harga+'):  # Ascending price
        idx = 4
        res = removeFirstElmt(game)
        res = sortMatrix(res, idx, '+')
        printGame(res, 1)
    elif (sorter == 'harga-'):  # Descending price
        idx = 4
        res = removeFirstElmt(game)
        res = sortMatrix(res, idx, '-')
        printGame(res, 1)
    else:  # If the sorting is not valid
        input("Skema sorting tidak valid")
    input("Press any key to continue...")
    return
