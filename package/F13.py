from .base import*

"""
    History Procedure   
"""


def history(user_id, riwayat):
    riwayat = removeFirstElmt(riwayat)  # Remove Header
    res = getUserHistory(user_id, riwayat)  # get user history

    if length(res) == 0:  # If riwayat is zero
        input("Kamu tidak memiliki riwayat pembelian. Ketik 7 pada menu utama untuk membeli game.")
    else:
        print_riwayat(res)
        input("Press any key to continue...")
