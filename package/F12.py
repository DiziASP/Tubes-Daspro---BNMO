from .base import*

"""
    Topup Procedure   
"""


def topup(user):
    while True:
        try:
            # Input username and saldo that want to be topped up
            username = validateUser(user)
            saldo = int(strip_str(input("Masukkan saldo: ")))

            # Traversing user array
            for i in range(0, length(user)):
                if user[i][1] == username:  # Match found
                    if int(user[i][5]) + saldo < 0:  # If saldo become zero
                        print("Masukkan tidak valid")
                        return
                    else:
                        user[i][5] = str(int(user[i][5]) + saldo)  # Add Saldo
                        input("Topup berhasil...")
                        return
        except ValueError:
            print("Input anda tidak valid. Silahkan ulangi input")
            continue
