# Import Necessary Library
import os
import argparse
import sys
import math
import time
import datetime

# Contains general function


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


# CSV Manager


def argParser():
    parser = argparse.ArgumentParser(description='argument')
    parser.add_argument('NamaFolder', type=str,
                        help='Folder Name Harus Diisi!')
    args = parser.parse_args()
    folder = args.NamaFolder
    return folder


def csv_reader(folder: str, filename: str) -> list:

    with open(f"./{folder}/{filename}.csv", "r") as f:
        next(f)
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

# Program related functions


def getRole(user_role: str) -> str:
    if(user_role == 'admin'):
        return 'admin'
    else:
        return 'user'
