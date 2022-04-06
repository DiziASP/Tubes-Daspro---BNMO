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

# Function tambahan


def length_mat(arr):
    counter = 0
    for i in arr:
        counter += 1
    return counter
