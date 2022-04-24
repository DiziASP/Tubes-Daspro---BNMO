from .base import *
"""
    Loading Procedure   
"""


def load():
    # Loading animation
    os.system("cls")
    sys.stdout.write('\rloading |')
    time.sleep(0.3)
    sys.stdout.write('\rloading /')
    time.sleep(0.3)
    sys.stdout.write('\rloading -')
    time.sleep(0.3)
    sys.stdout.write('\rloading \\')
    time.sleep(0.3)

    folder = argParser()  # Parsing from command line
    user = csv_reader(folder, "user")  # Read CSV and change into an array
    game = csv_reader(folder, "game")  # Read CSV and change into an array
    # Read CSV and change into an array
    kepemilikan = csv_reader(folder, "kepemilikan")
    # Read CSV and change into an array
    riwayat = csv_reader(folder, "riwayat")

    # Loading finished
    print('\rLoading berhasil...     ')
    time.sleep(0.3)
    input('\nPress any key to continue...     \n')
    return user, game, kepemilikan, riwayat
