from .base import*

"""
    Encryption Procedure using Homemade Cypher Algorithm
"""

lowerbound, upperbound = 32, 124


def encrypt(x):
    daftar_ord = []
    dev = 7
    for i in x:
        daftar_ord += [ord(i)]
    for j in range(len(daftar_ord)):
        check = 0
        check = daftar_ord[j] + dev
        if check != 59:
            if lowerbound <= check <= upperbound:
                pass
            else:
                check -= upperbound - lowerbound + 1
            daftar_ord[j] = check
        else:
            daftar_ord[j] = 126
        dev += 1

    return daftar_ord


def decrypt(x):
    daftar_ord = []
    dev = 7
    for i in x:
        daftar_ord += [ord(i)]
    for j in range(len(daftar_ord)):
        check = 0
        check = daftar_ord[j] - dev
        if check != 119:
            if lowerbound <= check <= upperbound:
                pass
            else:
                check += upperbound - lowerbound + 1
            daftar_ord[j] = check
        else:
            daftar_ord[j] = 59 - dev
        dev += 1
    return daftar_ord


def outputing(x):
    encrypted = ""
    for i in x:
        encrypted += chr(i)
    return encrypted
