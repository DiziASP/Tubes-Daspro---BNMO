from .base import*

"""
    Register Procedure   
"""


def register(user):
    id = getLastUserId(user) + 1
    username = validateUser(user)
    name = strip_str(input("Masukkan Nama: "))
    password = validatePassword()

    while validate(id) == True or validate(username) == True or validate(name) == True or validate(password) == True:
        print("Tidak boleh ada ; pada masukan. Silahkan ulangi kembali!")
        id = getLastUserId(user) + 1
        username = validateUser(user)
        name = strip_str(input("Masukkan Nama: "))
        password = validatePassword()
        
    new_user = [str(id), username, name, password, "user", '0']
    addObj(user, new_user)
    input("Registrasi sudah berhasil ^_^")
    return
