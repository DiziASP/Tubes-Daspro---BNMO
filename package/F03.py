from .base import*
"""
    Login Procedure   
"""


def login(user):
    while True:
        try:
            username_ = strip_str(input("Masukkan Username: "))
            password_ = strip_str(input("Masukkan Password: "))
            print(username_)
            for i in range(0, length(user)):
                if user[i][1] == username_ and user[i][3] == password_:
                    input(
                        f"Yeyy, kamu berhasil login. Selamat Datang {user[i][2]}!")
                    return True, user[i][1], user[i][3]
            else:
                print("Username anda tidak ditemukan atau password anda salah")
        except IndexError:
            print("Input anda tidak valid. Silahkan ulangi input!")
            continue
