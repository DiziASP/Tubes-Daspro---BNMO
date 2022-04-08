from .base import*


def ubah_game(game):
    nama = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis:")
    harga = input("Masukkan harga: ")

    for i in range(0, length(game)-1):
        if(length(nama) > 0):
            game[i][1] = nama
        if(length(kategori) > 0):
            game[i][2] = kategori
        if(length(tahun_rilis) > 0):
            game[i][3] = tahun_rilis
        if(length(harga) > 0):
            game[i][4] = harga
    input("Game berhasil diupdate!")
