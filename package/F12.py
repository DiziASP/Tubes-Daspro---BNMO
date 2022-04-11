from .base import*

"""
    Topup Procedure   
"""


def topup(user):
    while True:
        try:
            username = validateUser(user)
            saldo = int(strip_str(input("Masukkan saldo: ")))
            for i in range(0, length(user)):
                if user[i][1] == username:
                    if int(user[i][5]) + saldo < 0:
                        print("Masukkan tidak valid")
                        return
                    else:
                        user[i][5] = str(int(user[i][5]) + saldo)
                        input("Topup berhasil...")
                        return
        except ValueError:
            print("Input anda tidak valid. Silahkan ulangi input")
            continue
