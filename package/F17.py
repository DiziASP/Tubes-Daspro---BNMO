from .base import*
from .F16 import*

"""
    Exit Procedure   
"""


def exit_program(user, game, kepemilikan, riwayat):
    user_input = strip_str(
        input("Apakah anda ingin melakukan penyimpanan file?(y/n) "))
    var = ['y', 'Y', 'n', 'N']
    flag = True
    while not flag:
        for each in var:
            if each == user_input:
                flag = False
        print("Tolong berikan input yang benar atau nanti BNMO marah >:(")
        print("==============================================")
        user_input = strip_str(
            input("Apakah anda ingin melakukan penyimpanan file? "))
    if user_input.lower() == 'y':
        save(user, game, kepemilikan, riwayat)
    input("Terima kasih sudah bermain :D")
