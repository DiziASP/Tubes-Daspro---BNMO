from .base import*

"""
    User Game's List Procedure   
"""


def list_game(user_id, game, kepemilikan):
    game = removeFirstElmt(game)  # Remove header
    sorted = sortMatrix(game, 0, '+')  # Sort the matriks by ID

    # Search game owned by user
    game_owned = ownedByUser(user_id, kepemilikan)
    res = getOwnedGames(sorted, game_owned)

    # Validate
    if res == []:
        input(
            "Maaf kamu belum membeli game apapun. Ketik perintah 7 di main menu untuk membeli game")
    else:
        printGame(res, 2)  # Print User's game list
    input("Press any key to continue...")
