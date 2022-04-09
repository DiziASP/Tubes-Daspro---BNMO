from .base import*


def search_my_game(user_id, game, kepemilikan):
    id = input('Masukan ID Game: ')
    name = input('Masukan Nama Game: ')

    game = removeFirstElmt(game)
    game_owned = ownedByUser(user_id, kepemilikan)
    owned_games = getOwnedGames(sortMatrix(game, 0, '+'), game_owned)

    parameter = [[], []]
    res = []

    if id == '' and name == '':
        input("Parameter tidak boleh kosong. Silahkan isi minimal 1 parameter untuk menjalankan operasi ini")
        return

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

    for i in range(length(game)):
        if (game[i][0] in parameter[0] and
                game[i][1] in parameter[1] and game[i][0] in owned_games):
            addObj(res, game[i])

    if (length(res) != 0):
        printTable(res, 1)
    else:
        print("Tidak ada game yang memenuhi kriteria")
    input("Press any key to continue...")
