from .base import*


def print_riwayat(matrix: list):
    user_len = getLongestStrLen(matrix, 0)
    game_len = getLongestStrLen(matrix, 1)
    price_len = getLongestStrLen(matrix, 4)
    year_len = getLongestStrLen(matrix, 3)
    print("ID", " "*abs(user_len-length("ID")), "||",
          "Nama Game", " "*abs(game_len-length("Nama Game")), "||",
          "Harga", " "*abs(price_len - length("Harga")), "||",
          "Tahun Rilis", " " *
          abs(year_len-length("Tahun Rilis")))
    print("="*(user_len+game_len+price_len+year_len))
    for i in range(0, length(matrix)):
        print(matrix[i][0], " "*abs(user_len-length(matrix[i][0])), "||",
              matrix[i][1], " " * abs(game_len-length(matrix[i][1])), "||",
              matrix[i][2], " " * abs(price_len - length(matrix[i][4])), "||",
              matrix[i][4], " " * abs(year_len-length(matrix[i][3])),)


def getUserHistory(user_id, riwayat):
    res = []
    for each in riwayat:
        if each[3] == user_id:
            addObj(res, each)
    return res


def history(user_id, riwayat):
    if length(riwayat) == 0:
        input("Kamu tidak memiliki riwayat pembelian. Ketik 7 pada menu utama untuk membeli game.")
    riwayat = removeFirstElmt(riwayat)
    res = getUserHistory(user_id, riwayat)
    print(res)
    print_riwayat(res)
    input("Press any key to continue...")
