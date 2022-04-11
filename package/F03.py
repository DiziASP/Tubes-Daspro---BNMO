from .base import*
"""
    Login Procedure   
"""


def login(user):
    while True:
        try:
            username_ = strip_str(input("Masukkan Username: "))
            password_ = strip_str(input("Masukkan Password: "))
            for acc in user:
                if acc[1] == username_ and acc[3] == password_:
                    input(
                        f"Yeyy, kamu berhasil login. Selamat Datang {acc[2]}!")
                    return True, acc[0], acc[1]
            else:
                print("Username anda tidak ditemukan atau password anda salah")
        except ValueError:
            print("Input anda tidak valid. Silahkan ulangi input!")
            continue
