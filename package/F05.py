from .base import*

"""
    Change Game Procedure   
"""


def ubah_game(game):
    id = input("Masukkan ID game: ")
    nama = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis:")
    harga = input("Masukkan harga: ")

    while id == '':
        print("ID game tidak boleh kosong!")
        id = input("Masukkan ID game: ")
    if nama == "" and kategori == "" and tahun_rilis == "" and harga == "":
        input("Tidak ada game yang diubah")
        return

    for i in range(0, length(game)):
        if game[i][0] == id:
            if length(nama) > 0:
                game[i][1] = nama
            if(length(kategori) > 0):
                game[i][2] = kategori
            if(length(tahun_rilis) > 0):
                game[i][3] = tahun_rilis
            if(length(harga) > 0):
                game[i][4] = harga
    input("Game berhasil diupdate!")
    return
