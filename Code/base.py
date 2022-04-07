# Import Necessary Library
import os
import argparse
import sys
import math
import time
import datetime

# Function untuk membaca CSV


def spliter(line, delimiter):
    arr = []
    tmp = ''
    for c in line:
        if c == delimiter:
            arr.append(tmp)
            tmp = ''
        elif c == "\n":
            break
        else:
            tmp += c
    return arr


def csv_to_mat(filename):
    csv_to_array = []
    f = open(f'{filename}.csv', 'r')
    next(f)
    raw_lines = f.readlines()
    f.close()
    for raw_line in raw_lines:
        csv_to_array += [spliter(raw_line, ';')]

# Contains general function


def length(arr: list) -> int:
    count = 0

    for i in arr:
        count += 1
    return count


def add(list_par: list, param) -> int:
    list_par += [param]
    return list_par


def isUpper(param: str) -> bool:
    if param == param.upper():
        return True
    else:
        return False


def isLower(param: str) -> bool:
    if param == param.lower():
        return True
    else:
        return False


def conUpper(param: str) -> bool:
    res = False
    for i in param:
        if i == i.upper():
            res = True
            break
    return res


def conLower(param: str) -> bool:
    res = False
    for i in param:
        if i == i.lower():
            res = True
            break
    return res


def conNumber(param: str) -> bool:
    try:
        for i in param:
            n = int(i)
            return True
    except ValueError:
        return False
