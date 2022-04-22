"""
    Help Procedure   
"""


def Help(role):
    print('====================Need Help?====================')
    if role == 'admin':
        print('1. Login - Untuk login ke akun')
        print('2. Register - Untuk mendaftarkan akun')
        print('3. Tambah Game - Untuk menambah game yang dijual oleh toko')
        print('4. Ubah Game -  Untuk mengubah detail game')
        print('5. List Game Toko - Untuk melihat list game yang dijual toko')
        print('6. Ubah Stok -  Untuk mengubah stok game toko')
        print('7. List Game -  Untuk menampilkan list game yang dijual toko')
        print('8. Cari Game Toko -  Untuk mencari game di Toko')
        print('9. TopUp - Untuk menambahkan saldo User')
        print('10. Help -  Untuk melihat list command')
        print('11. Save - Menyimpan Data')
        print('12. Exit - Mengakhiri Program')
    elif role == "user":
        print('1. Login - Untuk login ke akun')
        print('2. List Game Toko - Untuk melihat list game yang dijual toko')
        print('3. Beli Game - Untuk membeli game di Toko')
        print('4. List Game User - Untuk melihat list game yang dimiliki')
        print('5. Search Game - Untuk mencari game yang dimiliki')
        print('6. Cari Game Toko -  Untuk mencari game di Toko')
        print('7. History - Melihat Riwayat Pembelian')
        print('8. Help -  Untuk melihat list command')
        print('9. Save - Menyimpan Data')
        print('10. Exit - Mengakhiri Program')
    else:
        print('1. Login - Untuk login ke akun')
        print('2. Help -  Untuk melihat list command')
