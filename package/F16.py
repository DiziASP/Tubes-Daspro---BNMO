from .base import*


def save(user, game, kepemilikan, riwayat):
    folder = input("Masukkan nama folder penyimpanan: ")
    create_folder(folder)
    write_csv(folder, user, "user")
    write_csv(folder, game, "game")
    write_csv(folder, kepemilikan, "kepemilikan")
    write_csv(folder, riwayat, "riwayat")

    input("Data berhasil tersimpan...")
