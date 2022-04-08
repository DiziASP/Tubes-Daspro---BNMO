from .base import*


def sortbyId(game):
    pass


def sortbyFilter(game, param):
    pass


def list_game_toko(game):
    sorter = input("""
                   Tahun+ || Tahun- 
                   harga+ || harga-
                   Masukkan Skema Pencarian:
                   """)
    if length(sorter) == 0:
        res = sortbyId(game)
