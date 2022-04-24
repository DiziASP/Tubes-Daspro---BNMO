from .base import*

"""
    Change Stock Procedure   
"""


def ubah_stok(game):
    try:
        # Validate ID
        while True:
            id = strip_str(input("Masukkan ID game: "))
            if(length(id) > 0):
                break
            print("Input ID tidak valid. Silahkan ulangi kembali")
        sum = int(strip_str(input("Masukkan jumlah: ")))  # Input Sum of stock

        game_, idx = getGamebyId(game, id)  # Get game by the Id Input by user
        if length(game_) == 0:  # If there is no id found
            input("Game dengan ID tersebut tidak ditemukan...")
        else:
            res = int(game_[5])+sum  # Add stock or reduce stock
            if res < 0:
                input(  # If the final stock is less than 0
                    f"Maaf, stok game {game[idx][1]} gagal dikurangi karena stok kurang. Stok sekarang adalah {game[idx][5]} ")
            else:
                game[idx][5] = str(res)
                input(
                    f"Stok game {game[idx][1]} berhasil diubah. Stok sekarang adalah {game[idx][5]}")
        return
    except ValueError and TypeError:
        input("Input anda tidak valid. Kembali ke Menu utama....")
        return
