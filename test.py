from package import*


def temp_load():
    user = csv_reader('dummy', "user")
    game = csv_reader('dummy', "game")
    kepemilikan = csv_reader('dummy', "kepemilikan")
    riwayat = csv_reader('dummy', "riwayat")
    return user, game, kepemilikan, riwayat


user, game, kepemilikan, riwayat = temp_load()
login(user)

login()
