from .base import*
from .constant import*
# Register


def validatePassword():
    while True:
        print(
            """Password harus : 
            - lebih dari 7 kata
            - mengandung huruf besar atau kecil
            - mengandung digit angka
            """)
        password_ = input("Masukkan Password: ")
        if not((conUpper(password_) or conLower(password_))
               and length(password_) > 8
                and conDigit(password_)):
            print("Password tidak sesuai dengan ketentuan. Silahkan coba kembali!")
        else:
            return password_


def validateUser():
    while True:
        username_ = input("Masukkan Username: ").rstrip()
        if not((conUpper(username_) or conLower(username_))
               and conSpec(username_)
               and conDigit(username_)):
            print("Username tidak sesuai dengan ketentuan. Silahkan coba kembali!")
        else:
            for i in range(0, length(user)):
                if(user[i][1] == username_):
                    print("Username ini sudah diambil. Gunakan username lain!")
            else:
                return username_


def register():
    id = length(user) + 1
    username = validateUser()
    name = input("Masukkan Nama: ")
    password = validatePassword()

    new_user = [str(id), username, name, password, "user", '0']
    addObj(user, new_user)

    print("Registrasi sudah berhasil. Selamat bermain ^_^")
