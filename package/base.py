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


def write_csv(folder, data, string):
    with open(f'./{folder}/{string}.csv', 'w') as f:
        tmp = []
        for i in range(length(data)):
            addObj(tmp, (';'.join(data[i])))
            addObj(tmp, '\n')
        res = ''.join(tmp)
        f.write(res)
        f.close()


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


def validateUser(user):
    while True:
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


def ValidateUserTopup(user):
    username_ = input("Masukkan Username: ").rstrip()
    if not((conUpper(username_) or conLower(username_))
           and conSpec(username_)
           and conDigit(username_)):
        print("Username tidak sesuai dengan ketentuan")
    else:
        for i in range(0, length(user)):
            if(user[i][1] == username_):
                print("Username ini sudah diambil. Gunakan username lain!")
                break
            else:
                return username_


def getGamebyId(game: list, game_id: str) -> list:
    count = 0
    for item in game:
        if item[0] == game_id:
            return item, count
        count += 1


def getUserById(user: list, user_id: str) -> list:
    count = 0
    for item in user:
        if item[0] == user_id:
            return item, count
        count += 1


def getValue(user, user_id):
    for i in range(len(user)):
        if user[i][0] == user_id:
            return user[i][5]
