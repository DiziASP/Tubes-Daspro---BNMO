from base import*
# Register

user = [[1, 'daspro1', 'A', '1234', 'admin', 20000],
        [2, 'daspro2', 'B', '1234', 'admin', 20000],
        [3, 'daspro3', 'C', '1234', 'user', 20000],
        [4, 'daspro4', 'D', '1234', 'user', 20000],
        [5, 'daspro5', 'E', '1234', 'user', 20000],
        [6, 'daspro6', 'F', '1234', 'user', 20000],
        [7, 'daspro7', 'G', '1234', 'user', 20000]
        ]


def validatePassword():
    while True:
        password = input("Masukkan Password: ")
        if (length(password) < 6):
            print("Password minimal harus terdiri dari 6 kata!")
        elif not any(ch.isupper() for ch in password):
            print(
                "Password minimal harus memiliki minimal 1 huruf besar dan huruf kecil!")
        elif not any(ch.islower() for ch in password):
            print(
                "Password minimal harus memiliki minimal 1 huruf besar dan huruf kecil!")
        elif not any(ch.isdigit() for ch in password):
            print("Password harus memiliki minimal 1 angka!")
        else:
            break

    return password


def validateUser():
    # Belum Kelar
    while True:
        username = input("Masukkan Username: ")
        ch = ['-', '_']
        checker = 0
        for i in range(length(username)):
            if(length(username) < 8 or username[i].isupper() or
               username[i].islower() or username[i] in ch or username[i].isdigit()):
                checker += 1

        if checker == length(username):
            for i in range(length(user)):
                if(username[i] == user[i][1]):
                    print("Username ini sudah terpakai")

    return username
# BELUM KELAR


def register():
    id = length(user) + 1
    username = input("Masukkan Username: ")
    name = input("Masukkan Nama: ")
    password = validatePassword()

    new_user = [id, username, name, password, "user", 0]
    add(user, new_user)

    print(user)


print(validatePassword())
