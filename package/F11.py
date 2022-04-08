from .base import*
from .constant import*


def search_game_at_store():
    id = input('Masukan ID Game: ')
    name = input('Masukan Nama Game: ')
    category = input('Masukan Kategori Game: ')
    price = input('Masukan Harga Game: ')
    year = input('Masukan Tahun rilis: ')

    search_res = []
    arr_param = [[], [], [], [], []]

    if id == '' and name == '' and price == '' and category == '' and year == '':
        print('Semua paramater tidak boleh kosong. Silahkan isi minimal 1 parameter!')
        return

    if length(id) > 0:
        arr_param[0] += [id]
    else:
        for i in range(length(game)):
            arr_param[0] += [game[i][0]]

    if length(name) > 0:
        arr_param[1] += [name]
    else:
        for i in range(length(game)):
            arr_param[1] += [game[i][1]]

    if length(price) > 0:
        arr_param[2] += [price]
    else:
        for i in range(length(game)):
            arr_param[2] += [game[i][4]]

    if length(category) > 0:
        arr_param[3] += [category]
    else:
        for i in range(length(game)):
            arr_param[3] += [game[i][2]]

    if length(year) > 0:
        arr_param[4] += [year]
    else:
        for i in range(length(game)):
            arr_param[4] += [game[i][3]]

    for i in range(length(game)):
        if game[i][0] in arr_param[0] and game[i][1] in arr_param[1] and game[i][4] in arr_param[2] and game[i][2] in arr_param[3] and game[i][3] in arr_param[4]:
            search_res += [game[i]]

    if length(search_res) != 0:
        print('Daftar game pada toko yang memenuhi kriteria:')
        for i in range(length(search_res)):
            print(search_res[i])

    else:
        print('Daftar game pada toko yang memenuhi kriteria:')
        print('Tidak ada game pada toko yang memenuhi kriteria')
