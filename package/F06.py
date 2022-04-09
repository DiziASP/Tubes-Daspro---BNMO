from .base import*


def ubah_stok(game):
    while True:
        id = input("Masukkan ID game: ")
        if(length(id) > 0):
            break
        print("Input ID tidak valid. Silahkan ulangi kembali")
    sum = int(input("Masukkan jumlah: "))

    stok, idx = getGamebyId(game, id)
    if length(stok) == 0:
        input("Game dengan ID tersebut tidak ditemukan...")
    else:
        res = int(stok[5])+sum
        if res < 0:
            input(
                f"Maaf, stok game {game[idx][1]} gagal dikurangi karena stok kurang. Stok sekarang adalah {game[idx][5]} ")
        else:
            game[idx][5] = str(res)
            input(
                f"Stok game {game[idx][1]} berhasil diubah. Stok sekarang adalah {game[idx][5]}")
