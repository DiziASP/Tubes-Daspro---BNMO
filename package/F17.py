from .base import*
from .F16 import*

"""
    Exit Procedure   
"""


def exit_program(user, game, kepemilikan, riwayat):
    user_input = strip_str(  # User choice yes or no
        input("Apakah anda ingin melakukan penyimpanan file?(y/n) "))

    var = ['y', 'Y', 'n', 'N']  # command
    flag = True  # Flag for founded in var
    while not flag:  # Validate input
        for each in var:
            if each == user_input:
                flag = False
        print("Tolong berikan input yang benar atau nanti BNMO marah >:(")
        print("==============================================")
        user_input = strip_str(
            input("Apakah anda ingin melakukan penyimpanan file? "))

    if user_input.lower() == 'y':  # If user wanted to save, run Save procedure
        save(user, game, kepemilikan, riwayat)
    input("Terima kasih sudah bermain :D")
