from .base import*


def tambah_game(game):
    while True:  # Validate Input
        nama = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun_rilis = input("Masukkan tahun rilis:")
        harga = input("Masukkan harga: ")
        stok = input("Masukkan stok awal: ")
        if (nama == '' or
            kategori == '' or
            tahun_rilis == '' or
            harga == '' or
                stok == ''):
            print("Mohon masukkan semua informasi mengenai game :() ")
            continue
        else:
            break
    game_data = [str(nama), str(kategori), str(
        tahun_rilis), str(harga), str(stok)]
    addObj(game, game_data)
    input("Game berhasil ditambahkan!")
