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


def validatePassword():
    pass


def validateUser():
    while True:
        username_ = input("Masukkan Username: ")
        if not((conUpper(username_) or conLower(username_))
               and conSpec(username_)
               and conDigit(username_)):
            print("Username tidak sesuai dengan ketentuan. Silahkan coba kembali!")
        else:
            return username_
