from .base import*


def history(user_id, riwayat):
    if length(riwayat) == 0:
        input("Kamu tidak memiliki riwayat pembelian. Ketik 7 pada menu utama untuk membeli game.")
    riwayat = removeFirstElmt(riwayat)
    res = getUserHistory(user_id, riwayat)
    print_riwayat(res)
    input("Press any key to continue...")
