from .base import*
from .B01 import outputing, encrypt

"""
    Register Procedure   
"""


def register(user):
    id = getLastUserId(user) + 1
    username = validateUser(user)
    name = strip_str(input("Masukkan Nama: "))
    password = validatePassword()
    while (length(str(id)) == 0
           or length(username) == 0
           or length(name) == 0
           or length(password) == 0):
        id = getLastUserId(user) + 1
        username = validateUser(user)
        name = strip_str(input("Masukkan Nama: "))
        password = validatePassword()

    new_user = [str(id), username, name, outputing(
        encrypt(password)), "user", '0']
    addObj(user, new_user)
    input("Registrasi sudah berhasil ^_^")
    return
