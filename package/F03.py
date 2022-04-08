from .base import*
from .constant import*
# Login


def login():
    while True:
        username_ = input("Masukkan Username: ")
        password_ = input("Masukkan Password: ")

        for acc in user:
            if acc[1] == username_ and acc[3] == password_:
                input(f"Yeyy, kamu berhasil login. Selamat Datang {acc[2]}")
                return True, acc
        else:
            print("Username anda tidak ditemukan atau password anda salah")
