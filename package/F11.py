from .base import*

"""
    Search Game at Store Procedure   
"""


def search_game_at_store(game):
    id = strip_str(input('Masukan ID Game: '))
    name = strip_str(input('Masukan Nama Game: '))
    price = strip_str(input('Masukan Harga Game: '))
    category = strip_str(input('Masukan Kategori Game: '))
    year = strip_str(input('Masukan Tahun rilis: '))

    while id == '' and name == '' and price == '' and category == '' and year == '':
        input("Parameter tidak boleh kosong. Silahkan isi minimal 1 parameter untuk menjalankan operasi ini")
        id = strip_str(input('Masukan ID Game: '))
        name = strip_str(input('Masukan Nama Game: '))
        price = strip_str(input('Masukan Harga Game: '))
        category = strip_str(input('Masukan Kategori Game: '))
        year = strip_str(input('Masukan Tahun rilis: '))
        game = removeFirstElmt(game)

    parameter = [[], [], [], [], []]
    res = []

    if length(id) > 0:
        addObj(parameter[0], id)
    else:
        for i in range(length(game)):
            addObj(parameter[0], game[i][0])

    if length(name) > 0:
        addObj(parameter[1], name)
    else:
        for i in range(length(game)):
            addObj(parameter[1], game[i][1])

    if length(price) > 0:
        addObj(parameter[2], price)
    else:
        for i in range(length(game)):
            addObj(parameter[4], game[i][4])

    if length(category) > 0:
        addObj(parameter[3], category)
    else:
        for i in range(length(game)):
            addObj(parameter[2], game[i][2])

    if length(year) > 0:
        addObj(parameter[3], year)
    else:
        for i in range(length(game)):
            addObj(parameter[3], game[i][3])

    for i in range(length(game)):
        if (game[i][0] in parameter[0] and
            game[i][1] in parameter[1] and
            game[i][2] in parameter[2] and
            game[i][3] in parameter[3] and
                game[i][4] in parameter[4]):
            addObj(res, game[i])

    if (length(res) > 0):
        printGame(res, 1)
    else:
        print("Tidak ada game yang memenuhi kriteria")
    input("Press any key to continue...")
