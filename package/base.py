"""
    Import Libraries
"""
import os
import argparse
import sys
import math
import time
import datetime

"""
    General Functions for program
"""


def length(arr: list) -> int:
    count = 0

    for i in arr:
        count += 1
    return count


def addObj(list_par: list, param) -> int:
    list_par += [param]
    return list_par


def conUpper(string: str) -> bool:
    res = False
    for each in string:
        if each == each.upper():
            res = True
            break
    return res


def conLower(string: str) -> bool:
    res = False
    for each in string:
        if each == each.lower():
            res = True
            break
    return res


def conDigit(string: str) -> bool:
    res = False
    num = ['0', '1', '2', '3', '4', '5',
           '6', '7', '8', '9']
    for each in string:
        if each in num:
            res = True
            break
    return res


def conSpec(string: str) -> bool:
    res = False
    special = ["-", "_"]
    for each in string:
        if each in special:
            res = True
            break
    return res


def absolute(num):
    if(num < 0):
        return -(num)
    else:
        return num


def removeFirstElmt(arr):
    res = []
    for i in range(length(arr)):
        if i == 0:
            continue
        res += [arr[i]]
    return res


"""
    Read and Write CSV function 
"""


def argParser():
    parser = argparse.ArgumentParser(description='argument')
    parser.add_argument('NamaFolder', type=str,
                        help='Folder Name Harus Diisi!')
    args = parser.parse_args()
    folder = args.NamaFolder
    return folder


def csv_reader(folder: str, filename: str) -> list:

    with open(f"./{folder}/{filename}.csv", "r") as f:
        result = []
        for each in f:
            row = []
            tmp = ""
            delimiter = ";"
            for ch in each:
                if ch == delimiter or ch == "\n":
                    row = addObj(row, tmp)
                    tmp = ""
                else:
                    tmp += ch
            result = addObj(result, row)
    return result


def create_folder(folder):
    path = "./"
    os.chdir(path)
    if not os.path.exists(folder):
        os.mkdir(folder)
    return


def write_csv(folder, data, string):
    with open(f'./{folder}/{string}.csv', 'w') as f:
        tmp = []
        for i in range(length(data)):
            addObj(tmp, (';'.join(data[i])))
            addObj(tmp, '\n')
        res = ''.join(tmp)
        f.write(res)
        f.close()
    return


"""
    Spesific Functions for program
"""


def printMenu():
    print("Selamat datang di interface BNMO ヽ(^◇^*)/")
    print("================Main Menu==================")
    print('1. Register')
    print('2. Login')
    print('3. Tambah Game')
    print('4. Ubah Game')
    print('5. Ubah Stok')
    print('6. List Game Toko')
    print('7. Buy Game')
    print('8. List Game User')
    print('9. Search My Game')
    print('10. Search Game At Store')
    print('11. Top Up')
    print('12. Riwayat')
    print('13. Help')
    print('14. Save')
    print('15. Exit')
    print('================Mini Games=================')
    print('16. Magic Conch Shell')
    print('17. Tic Tac Toe')
    print('===========================================')
    return


def getRole(user: list, user_id: str) -> str:
    for each in user:
        if each[0] == user_id:
            return each[4]


def getLastUserId(user_: list) -> int:
    for i in range(length(user_)):
        if i == length(user_)-1:
            return int(user_[i][0])


def validatePassword(user):
    while True:
        try:
            print(
                """
                Password harus : 
                - lebih dari 7 kata
                - mengandung huruf besar atau kecil
                - mengandung digit angka
                """)
            password_ = input("Masukkan Password: ")
            if not((conUpper(password_) or conLower(password_))
                   and length(password_) > 8
                    and conDigit(password_)):
                print("Password tidak sesuai dengan ketentuan. Silahkan coba kembali!")
            else:
                return password_
        except ValueError:
            print("Input anda tidak valid. Silahkan ulangi input")
            continue


def validateUser(user):
    while True:
        try:
            username_ = input("Masukkan Username: ").rstrip()
            if not((conUpper(username_) or conLower(username_))
                   and conSpec(username_)
                   and conDigit(username_)):
                print("Username tidak sesuai dengan ketentuan. Silahkan coba kembali!")
            else:
                for i in range(0, length(user)):
                    if(user[i][1] == username_):
                        print("Username ini sudah diambil. Gunakan username lain!")
                    else:
                        return username_
        except ValueError:
            print("Input anda tidak valid. Silahkan ulangi input")
            continue


def getGamebyId(game: list, game_id: str) -> list:
    count = 0
    for item in game:
        if item[0] == game_id:
            return item, count
        count += 1
    return


def getUserById(user: list, user_id: str) -> list:
    count = 0
    for item in user:
        if item[0] == user_id:
            return item, count
        count += 1
    return


def getValue(user, user_id):
    for i in range(len(user)):
        if user[i][0] == user_id:
            return user[i][5]


def isOnLibrary(user, game, kepemilikan):
    for item in kepemilikan:
        return (item[0] == game[0] and item[1] == user[0])


def write_riwayat(user_, game_, riwayat):
    year = datetime.datetime.today().year
    res = [game_[0], game_[1], game_[4], user_[0], str(year)]
    addObj(riwayat, res)


def sortMatrix(matrix: list, param: int, order: chr) -> list:
    if order == '+':
        for i in range(0, length(matrix)):
            for j in range(i+1, length(matrix)):
                if(int(matrix[i][param]) > int(matrix[j][param])):
                    matrix[i], matrix[j] = matrix[j], matrix[i]
        return matrix

    if order == '-':
        for i in range(0, length(matrix)):
            for j in range(i+1, length(matrix)):
                if(int(matrix[i][param]) < int(matrix[j][param])):
                    matrix[i], matrix[j] = matrix[j], matrix[i]
        return matrix


def getLongestStrLen(matrix: list, index: int) -> int:
    string = ''
    for i in range(length(matrix)):
        if length(matrix[i][index]) > length(string):
            string = matrix[i][index]
    return length(string)


def printGame(game_mat: list, list_type: int):
    id_len = getLongestStrLen(game_mat, 0)
    name_len = getLongestStrLen(game_mat, 1)
    price_len = getLongestStrLen(game_mat, 4)
    cat_len = getLongestStrLen(game_mat, 2)
    year_len = getLongestStrLen(game_mat, 3)
    stock_len = getLongestStrLen(game_mat, 5)

    if list_type == 1:
        print("ID", " "*abs(id_len-length("ID")), "||",
              "Nama Game", " "*abs(name_len-length("Nama Game")), "||",
              "Harga", " "*abs(price_len - length("Harga")), "||",
              "Kategori", " "*abs(cat_len-length("Kategori")), "||",
              "Tahun Rilis", " " * abs(year_len-length("Tahun Rilis")), "||",
              "Stok", " "*abs(stock_len-length("Stok")))
        print("="*(id_len+name_len+price_len+cat_len+year_len+stock_len+25))
        for i in range(0, length(game_mat)):
            print(game_mat[i][0], " "*abs(id_len-length(game_mat[i][0])), "||",
                  game_mat[i][1], " " *
                  abs(name_len-length(game_mat[i][1])), "||",
                  game_mat[i][4], " " *
                  abs(price_len - length(game_mat[i][4])), "||",
                  game_mat[i][2], " " *
                  abs(cat_len-length(game_mat[i][2])), "||",
                  game_mat[i][3], " " *
                  abs(year_len-length(game_mat[i][3])), "||",
                  game_mat[i][5], " "*abs(stock_len-length(game_mat[i][5])))

    if list_type == 2:
        print("ID", " "*abs(id_len-length("ID")), "||",
              "Nama Game", " "*abs(name_len-length("Nama Game")), "||",
              "Kategori", " "*abs(cat_len-length("Kategori")), "||",
              "Tahun Rilis", " " *
              abs(year_len-length("Tahun Rilis")), "||",
              "Harga", " "*abs(price_len - length("Harga")), "||",)
        print("="*(name_len+price_len+cat_len+year_len+stock_len+20))
        for i in range(1, length(game_mat)):
            print(game_mat[i][0], " "*abs(id_len-length(game_mat[i][0])), "||",
                  game_mat[i][1], " " *
                  abs(name_len-length(game_mat[i][1])), "||",
                  game_mat[i][2], " " *
                  abs(cat_len-length(game_mat[i][2])), "||",
                  game_mat[i][3], " " *
                  abs(year_len-length(game_mat[i][3])), "||",
                  game_mat[i][4], " "*abs(price_len - length(game_mat[i][4])))


def print_riwayat(matrix: list):
    user_len = getLongestStrLen(matrix, 0)
    game_len = getLongestStrLen(matrix, 1)
    price_len = getLongestStrLen(matrix, 4)
    year_len = getLongestStrLen(matrix, 3)
    print("ID", " "*abs(user_len-length("ID")), "||",
          "Nama Game", " "*abs(game_len-length("Nama Game")), "||",
          "Harga", " "*abs(price_len - length("Harga")), "||",
          "Tahun Beli", " " *
          abs(year_len-length("Tahun Beli")))
    print("="*(user_len+game_len+price_len+year_len))
    for i in range(0, length(matrix)):
        print(matrix[i][0], " "*abs(user_len-length(matrix[i][0])), "||",
              matrix[i][1], " " * abs(game_len-length(matrix[i][1])), "||",
              matrix[i][2], " " * abs(price_len - length(matrix[i][4])), "||",
              matrix[i][4], " " * abs(year_len-length(matrix[i][3])),)


def ownedByUser(user_id, kepemilikan):
    res = []
    for each in kepemilikan:
        if each[1] == user_id:
            res += each[0]
    return res


def getOwnedGames(arr, param):
    res = []
    for i in range(length(arr)):
        if arr[i][0] in param:
            res += arr[i]
    return res


def getUserHistory(user_id, riwayat):
    res = []
    for each in riwayat:
        if each[3] == user_id:
            addObj(res, each)
    return res
