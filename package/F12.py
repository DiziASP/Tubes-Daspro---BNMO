from .base import*


def topup(user):
    username = validateUser(user)
    saldo = int(input("Masukkan saldo: "))
    for i in range(0, length(user)):
        if user[i][1] == username:
            if int(user[i][5]) - saldo < 0:
                print("Masukkan tidak valid")
                break
            else:
                user[i][5] = str(int(user[i][5]) + saldo)
                break
    input("Topup berhasil...")
