from .B01 import outputing, encrypt
from .base import*
"""
    Login Procedure   
"""


def login(user):
    while True:
        try:
            # Input Data
            username_ = strip_str(input("Masukkan Username: "))
            password_ = strip_str(input("Masukkan Password: "))

            # Encrypt Pass
            encrypted = outputing(encrypt(password_))

            # Validate Username and password for login
            for i in range(0, length(user)):
                if user[i][1] == username_ and user[i][3] == encrypted:
                    input(
                        f"Yeyy, kamu berhasil login. Selamat Datang {user[i][2]}!")
                    # Return Login State, Logged User ID dan Username
                    return True, user[i][0], user[i][1]
            else:
                print("Username anda tidak ditemukan atau password anda salah")
        except IndexError:
            print("Input anda tidak valid. Silahkan ulangi input!")
            continue
