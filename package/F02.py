from .base import*
# Register


def register(user):
    id = getLastUserId(user) + 1
    username = validateUser(user)
    name = input("Masukkan Nama: ")
    password = validatePassword(user)

    new_user = [str(id), username, name, password, "user", '0']
    addObj(user, new_user)
    input("Registrasi sudah berhasil ^_^")
