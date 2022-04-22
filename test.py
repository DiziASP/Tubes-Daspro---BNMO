from package import*

user = csv_reader("Database", "user")
game = csv_reader("Database", "game")
kepemilikan = csv_reader("Database", "kepemilikan")
riwayat = csv_reader("Database", "riwayat")
buy_game('2', user, game, kepemilikan, riwayat)
