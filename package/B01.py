from .base import*

"""
    Encryption Procedure using Affine Cypher Algorithm
    MASIH ERROR COK
"""

a = 7
b = 3


def inverseModulo(a, m):
    for i in range(1, m):
        if((a % m)*(i % m) % m == 1):
            return i
    else:
        return -1


def encrypt(plaintext):
    res = ""
    for each in plaintext:
        tmp = (a*ord(each) + b) % 26
        res += chr(tmp)
    return res


def decrypt(cyphertext):
    inv_a = inverseModulo(a, 26)
    res = ""
    for each in cyphertext:
        tmp = inv_a*(ord(each) - b) % 26
        res += chr(tmp)
    return res
