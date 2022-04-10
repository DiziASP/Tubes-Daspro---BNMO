from .base import *
"""
    Loading Procedure   
"""


def load():
    os.system("cls")
    sys.stdout.write('\rloading |')
    time.sleep(0.3)
    sys.stdout.write('\rloading /')
    time.sleep(0.3)
    sys.stdout.write('\rloading -')
    time.sleep(0.3)
    sys.stdout.write('\rloading \\')
    time.sleep(0.3)

    folder = argParser()
    user = csv_reader(folder, "user")
    game = csv_reader(folder, "game")
    kepemilikan = csv_reader(folder, "kepemilikan")
    riwayat = csv_reader(folder, "riwayat")

    print('\rLoading berhasil...     ')
    time.sleep(0.3)
    input('\nPress any key to continue...     \n')
    return user, game, kepemilikan, riwayat
