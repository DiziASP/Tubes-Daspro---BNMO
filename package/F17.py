from .base import*
from .F16 import*

"""
    Exit Procedure   
"""


def exit_program(user, game, kepemilikan, riwayat):
    user_input = input("Apakah anda ingin melakukan penyimpanan file? ")
    var = ['y', 'Y', 'n', 'N']
    while True:
        if user_input in var:
            break
        user_input = input("Apakah anda ingin melakukan penyimpanan file? ")
    if user_input.lower() == 'y':
        save(user, game, kepemilikan, riwayat)
    input("Terima kasih sudah bermain :D")
