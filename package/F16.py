from .base import*

"""
    Savestrip_str( Procedure   
"""


def save(user, game, kepemilikan, riwayat):
    while True:
        try:
            folder = strip_str(
                input("Masukkan nama folder penyimpanan: "))  # Input folder
            while folder == '':  # Validate the input
                print("Input anda tidak valid. Silahkan ulangi kembali ya ges ya!")
                folder = strip_str(input("Masukkan nama folder penyimpanan: "))
            create_folder(folder)  # Check if the folder already exists or not
            write_csv(folder, user, "user")  # Write from array to csv
            write_csv(folder, game, "game")  # Write from array to csv
            # Write from array to csv
            write_csv(folder, kepemilikan, "kepemilikan")
            write_csv(folder, riwayat, "riwayat")  # Write from array to csv
            input("Data berhasil tersimpan...")
            return
        except ValueError:
            print("Tolong masukkan nama folder yang valid :>")
            continue
