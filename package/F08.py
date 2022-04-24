from .base import*

"""
    Buy Games Procedure   
"""


def buy_game(user_id, user, game, kepemilikan, riwayat):
    while True:
        try:
            # Input ID GAME
            game_id = strip_str(input("Masukkan ID Game: "))

            # Get user and game data
            user_, user_idx = getUserById(user, user_id)
            game_, game_idx = getGamebyId(game, game_id)
            saldo = int(getValue(user, user_id))
            harga = int(game_[4])

            # Validation
            if(isOnLibrary(user_, game_, kepemilikan)):
                input("Anda sudah memiliki game ini!")
            elif(saldo < harga):
                input("Saldo anda tidak cukup untuk membeli game ini!")
            elif(int(user[user_idx][5]) <= 0):
                input("Stok game tersebut sedang tidak ada")
            else:
                # If saldo is sufficient
                user[user_idx][4] = str(saldo - harga)  # Deduct saldo

                game[game_idx][5] = str(
                    int(game[game_idx][5])-1)  # Deduct stock

                # Write to kepemilikan
                write_kepemilikan(kepemilikan, user_idx, game_idx)
                write_riwayat(user[user_idx], game[game_idx],
                              riwayat)  # write to riwayat
                input(f"Game {game_[1]} telah berhasil dibeli!")
            return
        except TypeError:
            print("ID tidak valid. Silahkan ulangi")
            continue
