from package import*


def temp_load():
    user = csv_reader('dummy', "user")
    game = csv_reader('dummy', "game")
    kepemilikan = csv_reader('dummy', "kepemilikan")
    riwayat = csv_reader('dummy', "riwayat")
    return user, game, kepemilikan, riwayat


def temp_login(user):
    while True:
        try:
            username_ = strip_str(input("Masukkan Username: "))
            password_ = strip_str(input("Masukkan Password: "))
            for i in range(0, length(user)):
                if user[i][1] == username_ and user[i][3] == password_:
                    input(
                        f"Yeyy, kamu berhasil login. Selamat Datang {user[i][2]}!")
                    return True, user[i][0], user[i][2]
            else:
                print("Username anda tidak ditemukan atau password anda salah")
        except IndexError:
            print("Input anda tidak valid. Silahkan ulangi input!")
            continue


user, game, kepemilikan, riwayat = temp_load()

isLogged, current_id, current_username = temp_login(user)
print(user)
role = getRole(user, current_id)
print(role)
