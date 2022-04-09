from .base import*


def ubah_stok(game):
    try:
        while True:
            id = input("Masukkan ID game: ")
            if(length(id) > 0):
                break
            print("Input ID tidak valid. Silahkan ulangi kembali")
        sum = int(input("Masukkan jumlah: "))

        game_, idx = getGamebyId(game, id)
        if length(game_) == 0:
            input("Game dengan ID tersebut tidak ditemukan...")
        else:
            res = int(game_[5])+sum
            if res < 0:
                input(
                    f"Maaf, stok game {game[idx][1]} gagal dikurangi karena stok kurang. Stok sekarang adalah {game[idx][5]} ")
            else:
                game[idx][5] = str(res)
                input(
                    f"Stok game {game[idx][1]} berhasil diubah. Stok sekarang adalah {game[idx][5]}")
        return
    except ValueError:
        input("Input anda tidak valid. Kembali ke Menu utama....")
        return
