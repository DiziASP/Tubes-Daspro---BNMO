from .base import*

"""
    Search My Game Procedure   
"""


def search_my_game(user_id, game, kepemilikan):
    # Input game data
    id = strip_str(input('Masukan ID Game: '))
    tahun_rilis = strip_str(input('Masukan Tahun Rilis Game: '))

    # Validate input
    while id == '' and tahun_rilis == '':
        input("Parameter tidak boleh kosong. Silahkan isi minimal 1 parameter untuk menjalankan operasi ini")
        id = strip_str(input('Masukan ID Game: '))
        tahun_rilis = strip_str(input('Masukan Nama Game: '))

    game = removeFirstElmt(game)  # Remove header
    # Search game owned by user
    game_owned = ownedByUser(user_id, kepemilikan)
    owned_games = getOwnedGames(game, game_owned)

    res = []  # Temporary Variable to hold games that matched the criteria
    for i in range(0, length(owned_games)):
        if owned_games[i][0] == id or owned_games[i][3] == tahun_rilis:
            res += [owned_games[i]]  # Add game to res
    if (length(res) != 0):
        printGame(res, 2)
    else:  # If the temporary array is empty aka no match found
        print("Tidak ada game yang memenuhi kriteria")
    input("Press any key to continue...")
