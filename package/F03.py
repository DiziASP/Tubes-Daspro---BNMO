from .base import*
from .constant import*
# Login


def login():
    while True:
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        for acc in user:
            if acc[1] == username and acc[3] == password:
                print(f"Login berhasil. Selamat Datang {acc[2]}")
                return True
        else:
            print("Username anda tidak ditemukan atau password anda salah")
