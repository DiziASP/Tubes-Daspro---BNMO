from .base import*

"""
    Add Game Procedure   
"""


def tambah_game(game):
    while True:  # Validate Input
        nama = strip_str(input("Masukkan nama game: "))
        kategori = strip_str(input("Masukkan kategori: "))
        tahun_rilis = strip_str(input("Masukkan tahun rilis:"))
        harga = strip_str(input("Masukkan harga: "))
        stok = strip_str(input("Masukkan stok awal: "))
        if (nama == '' or kategori == '' or tahun_rilis == '' or
                harga == '' or stok == ''):
            print(
                "Mohon masukkan semua informasi mengenai game dan tidak boleh ada ; pada tiap informasi")
            continue
        else:
            break

    # Get ID
    sorted = removeFirstElmt(game)
    sorted = sortMatrix(sorted, 0, '+')
    id = int(sorted[length(sorted)-1][0]) + 1

    # Create array for new game
    game_data = [str(id), str(nama), str(kategori), str(
        tahun_rilis), str(harga), str(stok)]
    addObj(game, game_data)  # Add new game
    input("Game berhasil ditambahkan!")
    return
