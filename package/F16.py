from .base import*

"""
    Save Procedure   
"""


def save(user, game, kepemilikan, riwayat):
    while True:
        try:
            folder = input("Masukkan nama folder penyimpanan: ")
            create_folder(folder)
            write_csv(folder, user, "user")
            write_csv(folder, game, "game")
            write_csv(folder, kepemilikan, "kepemilikan")
            write_csv(folder, riwayat, "riwayat")
            input("Data berhasil tersimpan...")
            return
        except ValueError:
            print("Tolong masukkan nama folder yang valid :>")
            continue
