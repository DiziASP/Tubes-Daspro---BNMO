from .base import*


def list_game(user_id, game, kepemilikan):
    sorted = sortMatrix(game, 0, '+')
    game_owned = ownedByUser(user_id, kepemilikan)
    res = getOwnedGames(sorted, game_owned)
    if res == []:
        input("Maaf kamu belum membeli game ini. Ketik perintah 7 di main menu untuk membeli game")
    else:
        printGame(res, 2)
    input("Press any key to continue...")
