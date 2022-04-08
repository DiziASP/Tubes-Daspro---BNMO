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
"""Badok dari gugel, tiati masih rentan plagi"""


def argParser():
    parser = argparse.ArgumentParser(description='argument')
    parser.add_argument('NamaFolder', type=str,
                        help='Folder Name Harus Diisi!')
    args = parser.parse_args()
    folder = args.NamaFolder
    return folder


def csv_to_mat(folder: str, filename: str) -> list:
    if filename == 'user' or filename == 'game':
        col = 6
    elif filename == 'kepemilikan':
        col = 2
    elif filename == 'riwayat':
        col = 5

    with open(f'./{folder}/{filename}.csv', 'r') as f:
        next(f)
        res = []
        delimiter = ';'
        for row in f:
            row = row.rstrip()
            tmp = ''
            for ch in row:
                if(ch == delimiter):
                    res += [tmp]
                    tmp = ''
                else:
                    tmp += ch
            res += [tmp]
        # Matrix
        matrix = [["" for j in range(col)] for i in range(length(res)//col)]
        num = 0
        for i in range(length(res)//col):
            for j in range(col):
                matrix[i][j] = res[num]
                num += 1
            if num == length(res):
                break
        return matrix
