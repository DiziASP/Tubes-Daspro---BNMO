from .base import *
# Load


def load():
    while True:
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
        break
    print('\rLoading berhasil...     ')
    time.sleep(0.3)
    input('\nPress any key to continue...     \n')
    return user, game, kepemilikan, riwayat