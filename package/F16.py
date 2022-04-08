from .base import*
from .constant import*


def save():
    user_ = user
    game_ = game
    kepemilikan_ = kepemilikan
    riwayat_ = riwayat

    folder = input("Masukkan nama folder penyimpanan: ")
    create_folder(folder)
    write_csv(folder, user_, "user")
    write_csv(folder, game_, "game")
    write_csv(folder, kepemilikan_, "kepemilikan")
    write_csv(folder, riwayat_, "riwayat")

    input("Data berhasil tersimpan...")
