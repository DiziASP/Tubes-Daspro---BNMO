from .base import*


def list_game_toko(game):
    sorter = input(
        """
        Tahun+ || Tahun- 
        harga+ || harga-
        Masukkan Skema Pencarian:
        """)
    if length(sorter) == 0:
        idx = 0
        res = sortMatrix(game, idx, '+')
        res = removeFirstElmt(res)
        printTable(res, 1)
    elif (sorter == 'tahun+'):
        idx = 4
        res = sortMatrix(game, idx, '+')
        res = removeFirstElmt(res)
        printTable(res, 1)
    elif (sorter == 'tahun-'):
        idx = 4
        res = sortMatrix(game, idx, '-')
        res = removeFirstElmt(res)
        printTable(res, 1)
    elif (sorter == 'harga+'):
        idx = 5
        res = sortMatrix(game, idx, '+')
        res = removeFirstElmt(res)
        printTable(res, 1)
    elif (sorter == 'harga-'):
        idx = 5
        res = sortMatrix(game, idx, '-')
        res = removeFirstElmt(res)
        printTable(res, 1)
    else:
        input("Skema sorting tidak valid")
    input("Press any key to continue...")
