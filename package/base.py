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
    element = 0
    for each in arr:
        element += 1
    return element


def addObj(list_par: list, param) -> int:
    list_par += [param]
    return list_par


def conUpper(string: str) -> bool:
    res = False
    for i in range(0, length(string)):
        if string[i] == string[i].upper():
            res = True
            break
    return res


def conLower(string: str) -> bool:
    res = False
    for i in range(0, length(string)):
        if string[i] == string[i].lower():
            res = True
            break
    return res


def conDigit(string: str) -> bool:
    res = False
    num = ['0', '1', '2', '3', '4', '5',
           '6', '7', '8', '9']
    for i in range(0, length(string)):
        for j in range(0, length(num)):
            if string[i] == num[j]:
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


def absolute(num: int) -> int:
    if(num < 0):
        return -(num)
    else:
        return num


def strip_str(s: str) -> list:
    if(length(s) == 0):
        return ""
    res = ""
    begin = 0
    end = length(s)-1
    while s[begin] == " ":
        begin += 1
    while s[end] == " ":
        end -= 1
    end += 1
    for i in range(begin, end):
        res += s[i]
    return res


def removeFirstElmt(arr: list) -> list:
    res = []
    for i in range(length(arr)):
        if i == 0:
            continue
        res += [arr[i]]
    return res


def LCG():
    m = 12  # Modulus {m > 0}
    a = 9   # multiplier {0 <= a <= m }
    x = int(time.time()) % m  # Xo {0 <= xo <= m}
    # incrementor {0 <= c < m , c = 0 means Lehmer RNG Algorithm}
    c = int(time.process_time_ns()) % m
    return (a*x+c) % m


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

    with open(f"./{folder}/{filename}.csv", "r", encoding='utf-8-sig') as f:
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


def create_folder(folder: str):
    path = "./"
    os.chdir(path)
    if not os.path.exists(folder):
        os.mkdir(folder)
    return


def write_csv(folder: str, data: list, string: str):
    with open(f'./{folder}/{string}.csv', 'w', encoding='utf-8-sig') as f:
        res = ''
        for i in range(length(data)):
            for j in range(length(data[i])):
                if j == length(data[i]) - 1:
                    res += str(data[i][j])
                else:
                    res += f"{data[i][j]};"
            res += "\n"
        f.write(res)
        f.close()
    return


"""
    Spesific Functions for program
"""


def printMenu():
    print("Selamat datang di interface BNMO ヽ(^◇^*)/")
    print("================Main Menu==================")
    print('-> Register')
    print('-> Login')
    print('-> Tambah Game')
    print('-> Ubah Game')
    print('-> Ubah Stok')
    print('-> List Game Toko')
    print('-> Buy Game')
    print('-> List Game User')
    print('-> Search My Game')
    print('-> Search Game At Store')
    print('-> Top Up')
    print('-> Riwayat')
    print('-> Help')
    print('-> Save')
    print('-> Exit')
    print('================Mini Games=================')
    print('-> Magic Conch Shell')
    print('-> Tic Tac Toe')
    print('===========================================')
    return


def getRole(user: list, user_id: str) -> str:
    for i in range(0, length(user)):
        if user[i][0] == user_id:
            return user[i][4]


def getLastUserId(user_: list) -> int:
    for i in range(length(user_)):
        if i == length(user_)-1:
            return int(user_[i][0])
    else:
        return 1


def validatePassword():
    while True:
        try:
            print(
                """
                Password harus : 
                - lebih dari 7 kata
                - mengandung huruf besar atau kecil
                - mengandung digit angka
                """)
            password_ = strip_str(input("Masukkan Password: "))
            if not((conUpper(password_) or conLower(password_))
                   and length(password_) > 8
                    and conDigit(password_)):
                print("Password tidak sesuai dengan ketentuan. Silahkan coba kembali!")
            else:
                return password_
        except ValueError:
            print("Input anda tidak valid. Silahkan ulangi input")
            continue


def validateUser(user: list) -> str:
    while True:
        try:
            username_ = strip_str(input("Masukkan Username: "))
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
    for i in range(0, length(game)):
        if game[i][0] == game_id:
            return game[i], count
        count += 1
    return


def getUserById(user: list, user_id: str) -> list:
    count = 0
    for i in range(0, length(user)):
        if user[i][0] == user_id:
            return user[i], count
        count += 1
    return


def getValue(user: list, user_id: str) -> str:
    for i in range(len(user)):
        if user[i][0] == user_id:
            return user[i][5]


def isOnLibrary(user: list, game: list, kepemilikan: list) -> bool:
    for i in range(0, length(kepemilikan)):
        return (kepemilikan[i][0] == game[0] and kepemilikan[i][1] == user[0])


def write_riwayat(user_: list, game_: list, riwayat: list):
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
    for i in range(0, length(matrix)):
        if length(matrix[i][index]) > length(string):
            string = matrix[i][index]
    return length(string)


def whole_numerate(n):
    return math.ceil((abs(n)+n)/2)


def printGame(game_mat: list, list_type: int):
    stock_len = (length("Stok"), getLongestStrLen(game_mat, 5))[
        getLongestStrLen(game_mat, 5) > length("Stok")]
    id_len = (length("ID"), getLongestStrLen(game_mat, 0))[
        getLongestStrLen(game_mat, 0) > length("ID")]
    name_len = (length("Nama Game"), getLongestStrLen(game_mat, 1))[
        getLongestStrLen(game_mat, 1) > length("Nama Game")]
    price_len = (length("Harga"), getLongestStrLen(game_mat, 4))[
        getLongestStrLen(game_mat, 4) > length("Harga")]
    cat_len = (length("Kategori"), getLongestStrLen(game_mat, 2))[
        getLongestStrLen(game_mat, 2) > length("Kategori")]
    year_len = (length("Tahun Rilis"), getLongestStrLen(game_mat, 3))[
        getLongestStrLen(game_mat, 3) > length("Tahun Rilis")]

    if list_type == 1:
        print("ID", " "*(id_len-length("ID")), "|",
              "Nama Game", " "*(name_len-length("Nama Game")), "|",
              "Harga", " "*(price_len-length("Harga")), "|",
              "Kategori", " "*(cat_len-length("Kategori")), "|",
              "Tahun Rilis", " " * (year_len-length("Tahun Rilis")), "|",
              "Stok", " "*(stock_len-length("Stok")))
        print("="*(id_len+name_len+price_len+cat_len+year_len+stock_len+25))
        for i in range(0, length(game_mat)):
            print(game_mat[i][0], " "*whole_numerate(int(id_len)-length(game_mat[i][0])), "|",
                  game_mat[i][1], " " *
                  whole_numerate(int(name_len)-length(game_mat[i][1])), "|",
                  game_mat[i][4], " " *
                  whole_numerate(int(price_len)-length(game_mat[i][4])), "|",
                  game_mat[i][2], " " *
                  whole_numerate(int(cat_len)-length(game_mat[i][2])), "|",
                  game_mat[i][3], " " *
                  whole_numerate(int(year_len)-length(game_mat[i][3])), "|",
                  game_mat[i][5], " "*whole_numerate(int(id_len)-length(game_mat[i][5])))

    if list_type == 2:
        print("ID", " "*(id_len-length("ID")), "|",
              "Nama Game", " "*(name_len-length("Nama Game")), "|",
              "Harga", " "*(price_len-length("Harga")), "|",
              "Kategori", " "*(cat_len-length("Kategori")), "|",
              "Tahun Rilis", " " * (year_len-length("Tahun Rilis")))
        print("="*(id_len+name_len+price_len+cat_len+year_len+25))
        for i in range(0, length(game_mat)):
            print(game_mat[i][0], " "*whole_numerate(int(id_len)-length(game_mat[i][0])), "|",
                  game_mat[i][1], " " *
                  whole_numerate(int(name_len)-length(game_mat[i][1])), "|",
                  game_mat[i][4], " " *
                  whole_numerate(int(price_len)-length(game_mat[i][4])), "|",
                  game_mat[i][2], " " *
                  whole_numerate(int(cat_len)-length(game_mat[i][2])), "|",
                  game_mat[i][3], " " * whole_numerate(int(year_len)-length(game_mat[i][3])))


def print_riwayat(matrix: list):
    id_len = (length("ID"), getLongestStrLen(matrix, 0))[
        getLongestStrLen(matrix, 0) > length("ID")]
    game_len = (length("Nama Game"), getLongestStrLen(matrix, 1))[
        getLongestStrLen(matrix, 1) > length("ID")]
    price_len = (length("Harga"), getLongestStrLen(matrix, 4))[
        getLongestStrLen(matrix, 4) > length("Harga")]
    year_len = (length("Tahun Pembelian"), getLongestStrLen(matrix, 3))[
        getLongestStrLen(matrix, 3) > length("Tahun Pembelian")]
    print("ID", " "*(id_len-length("ID")), "|",
          "Nama Game", " "*(game_len-length("Nama Game")), "|",
          "Harga", " "*(price_len - length("Harga")), "|",
          "Tahun Beli", " " * (year_len-length("Tahun Beli")))
    print("="*(id_len+game_len+price_len+year_len))
    for i in range(0, length(matrix)):
        print(matrix[i][0], " "*whole_numerate(int(id_len)-length(matrix[i][0])), "|",
              matrix[i][1], " " *
              whole_numerate(int(game_len)-length(matrix[i][1])), "|",
              matrix[i][2], " " *
              whole_numerate(int(price_len)-length(matrix[i][2])), "|",
              matrix[i][4], " " * whole_numerate(int(year_len)-length(matrix[i][4])),)


def ownedByUser(user_id: str, kepemilikan: list) -> list:
    res = []
    for i in range(0, length(kepemilikan)):
        if kepemilikan[i][1] == user_id:
            res += kepemilikan[i][0]
    return res


def getOwnedGames(arr: list, param: list) -> list:
    res = []
    for i in range(length(arr)):
        for each in param:
            if arr[i][0] == each:
                res += [arr[i]]
    return res


def getUserHistory(user_id: str, riwayat: list) -> list:
    res = []
    for i in range(0, length(riwayat)):
        if riwayat[i][3] == user_id:
            addObj(res, riwayat[i])
    return res
