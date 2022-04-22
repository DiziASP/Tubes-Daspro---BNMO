from .base import*

"""
    Search My Game Procedure   
"""


def search_my_game(user_id, game, kepemilikan):
    id = strip_str(input('Masukan ID Game: '))
    name = strip_str(input('Masukan Nama Game: '))

    while id == '' and name == '':
        input("Parameter tidak boleh kosong. Silahkan isi minimal 1 parameter untuk menjalankan operasi ini")
        id = strip_str(input('Masukan ID Game: '))
        name = strip_str(input('Masukan Nama Game: '))

    game = removeFirstElmt(game)
    game_owned = ownedByUser(user_id, kepemilikan)
    owned_games = getOwnedGames(game, game_owned)
    res = []

    for i in range(0, length(owned_games)):
        if owned_games[i][0] == id or owned_games[i][1] == name:
            res += [owned_games[i]]
    if (length(res) != 0):
        printGame(res, 1)
    else:
        print("Tidak ada game yang memenuhi kriteria")
    input("Press any key to continue...")
