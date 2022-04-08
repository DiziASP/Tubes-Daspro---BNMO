from .base import *
# Load


def load():
    folder = argParser()
    user = csv_to_mat(folder, "user")
    game = csv_to_mat(folder, "game")
    kepemilikan = csv_to_mat(folder, "kepemilikan")
    riwayat = csv_to_mat(folder, "riwayat")
    return user, game, kepemilikan, riwayat
