from .base import*
from .B01 import outputing, encrypt

"""
    Register Procedure   
"""


def register(user):
    # Input Data
    id = getLastUserId(user) + 1
    username = validateUser(user)
    name = strip_str(input("Masukkan Nama: "))
    password = validatePassword()

    # Validate input
    while (length(str(id)) == 0
           or length(username) == 0
           or length(name) == 0
           or length(password) == 0):
        id = getLastUserId(user) + 1
        username = validateUser(user)
        name = strip_str(input("Masukkan Nama: "))
        password = validatePassword()

    # Create array for new user
    new_user = [str(id), username, name, outputing(
        encrypt(password)), "user", '0']
    addObj(user, new_user)  # Add new user
    input("Registrasi sudah berhasil ^_^")
    return
