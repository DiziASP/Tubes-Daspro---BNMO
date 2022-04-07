from sqlalchemy import true
from base import*
from constant import*
# Register


def register():
    id = length(user) + 1
    username = validateUser()
    name = input("Masukkan Nama: ")
    password = input("Masukkan Password: ")

    new_user = [str(id), username, name, password, "user", '0']
    addObj(user, new_user)

    print("Registrasi sudah berhasil. Selamat bermain ^_^")
