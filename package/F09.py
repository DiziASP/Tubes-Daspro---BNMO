from .base import*

"""
    User Game's List Procedure   
"""


def list_game(user_id, game, kepemilikan):
    game = removeFirstElmt(game)
    sorted = sortMatrix(game, 0, '+')
    game_owned = ownedByUser(user_id, kepemilikan)
    res = getOwnedGames(sorted, game_owned)
    if res == []:
        input("Maaf kamu belum membeli game ini. Ketik perintah 7 di main menu untuk membeli game")
    else:
        printGame(res, 2)
    input("Press any key to continue...")
