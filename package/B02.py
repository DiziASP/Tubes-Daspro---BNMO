from .base import*

"""
    Magic Conch Shell Procedure   
"""


def kerangajaib():
    os.system("cls")  # Clear the console
    while True:
        try:
            q = strip_str(input("Apa pertanyaanmu? "))  # User Input
            lcg = LCG()  # Randomize using Linear Congruential Generator

            if q == '':  # If the input is empty, exit the procedure
                input("ok")
                return
            else:
                ans = ['Y', 'G', 'Mayhaps', 'g dl y ges y', 'yntkts',  # Random Answer
                       'Mungkin', 'Oh jelas', 'p mkst?', 'dih, apaan dah ◔_◔']
                print(ans[lcg % 8])  # Print Answer
        except ValueError:
            print("Input mu ndak valid mas e")
            continue
