from .base import*

"""
    Magic Conch Shell Procedure   
"""


def kerangajaib():
    while True:
        try:
            q = strip_str(input("Apa pertanyaanmu? "))
            lcg = LCG()

            if q == ' ':
                input("ok")
                return
            else:
                ans = ['Y', 'G', 'Mayhaps', 'g dl', 'yntkts',
                       'Mungkin', 'Oh jelas', 'p mkst?', 'dih, apaan dah ◔_◔']
                print(ans[lcg % 8])
        except ValueError:
            print("Input mu ndak valid mas e")
            continue