from .base import*

"""
    Search Game at Store Procedure   
"""


def search_game_at_store(game):
    # Input data
    id = strip_str(input('Masukan ID Game: '))
    name = strip_str(input('Masukan Nama Game: '))
    price = strip_str(input('Masukan Harga Game: '))
    category = strip_str(input('Masukan Kategori Game: '))
    year = strip_str(input('Masukan Tahun rilis: '))

    # Validate Input
    while id == '' and name == '' and price == '' and category == '' and year == '':
        input("Parameter tidak boleh kosong. Silahkan isi minimal 1 parameter untuk menjalankan operasi ini")
        id = strip_str(input('Masukan ID Game: '))
        name = strip_str(input('Masukan Nama Game: '))
        price = strip_str(input('Masukan Harga Game: '))
        category = strip_str(input('Masukan Kategori Game: '))
        year = strip_str(input('Masukan Tahun rilis: '))

    game = removeFirstElmt(game)  # remove header

    parameter = [[], [], [], [], []]  # Array to store parameter by user input
    res = []  # array to store filter result

    if length(id) > 0:  # Filter by ID
        addObj(parameter[0], id)
    else:
        for i in range(length(game)):
            addObj(parameter[0], game[i][0])

    if length(name) > 0:  # Filter by Name
        addObj(parameter[1], name)
    else:
        for i in range(length(game)):
            addObj(parameter[1], game[i][1])

    if length(price) > 0:  # Filter by Price
        addObj(parameter[2], price)
    else:
        for i in range(length(game)):
            addObj(parameter[4], game[i][4])

    if length(category) > 0:  # Filter by Category
        addObj(parameter[3], category)
    else:
        for i in range(length(game)):
            addObj(parameter[2], game[i][2])

    if length(year) > 0:  # Filter by Year
        addObj(parameter[3], year)
    else:
        for i in range(length(game)):
            addObj(parameter[3], game[i][3])

    for i in range(length(game)):
        #  Boolean to store flags
        bool1 = False
        bool2 = False
        bool3 = False
        bool4 = False
        bool5 = False

        for each in parameter[0]:
            if game[i][0] == each:
                bool1 = True
        for each in parameter[1]:
            if game[i][1] == each:
                bool2 = True
        for each in parameter[2]:
            if game[i][2] == each:
                bool3 = True
        for each in parameter[3]:
            if game[i][3] == each:
                bool4 = True
        for each in parameter[4]:
            if game[i][4] == each:
                bool5 = True
        if (bool1 and bool2 and bool3 and bool4 and bool5):  # If the game match all parameters
            addObj(res, game[i])

    if (length(res) > 0):
        printGame(res, 1)  # Print searched game
    else:
        print("Tidak ada game yang memenuhi kriteria")
    input("Press any key to continue...")
