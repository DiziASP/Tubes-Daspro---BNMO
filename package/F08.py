from .base import*

"""
    Buy Games Procedure   
"""


def buy_game(user_id, user, game, kepemilikan, riwayat):
    game_id = strip_str(input("Masukkan ID Game: "))
    user_, user_idx = getUserById(user, user_id)
    game_, game_idx = getGamebyId(game, game_id)

    # Validation
    saldo = int(getValue(user, user_id))
    harga = int(game_[4])
    if(isOnLibrary(user_, game_, kepemilikan)):
        input("Anda sudah memiliki game ini!")
    elif(saldo < harga):
        input("Saldo anda tidak cukup untuk membeli game ini!")
    elif(int(user[user_idx][5]) <= 0):
        input("Stok game tersebut sedang tidak ada")
    else:
        user[user_idx][4] = str(saldo - harga)

        game[game_idx][5] = str(int(game[game_idx][5])-1)

        write_kepemilikan(kepemilikan, user_idx, game_idx)
        write_riwayat(user[user_idx], game[game_idx], riwayat)
        input(f"Game {game_[1]} telah berhasil dibeli!")
    return
