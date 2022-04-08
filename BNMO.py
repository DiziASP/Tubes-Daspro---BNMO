from package import*

if __name__ == "__main__":
    """
        Running the Main Program
    """
    isLogged = False  # Login Status
    user = []   # Initiate User

    while True:
        os.system('cls')  # Clear Console

        # Main Menu
        print("Selamat datang di interface BNMO ヽ(^◇^*)/")
        print("================Main Menu==================")
        print('1. Register')
        print('2. Login')
        print('3. Tambah Game')
        print('4. Ubah Game')
        print('5. Ubah Stok')
        print('6. List Game Toko')
        print('7. Buy Game')
        print('8. List Game User')
        print('9. Search My Game')
        print('10. Search Game At Store')
        print('11. Top Up')
        print('12. Riwayat')
        print('13. Help')
        print('14. Save')
        print('15. Exit')
        print('================Mini Games=================')
        print('16. Magic Conch Shell')
        print('17. Tic Tac Toe')
        print('=========================================================')

        # Choose Menu
        user_input = input("Silahkan pilih menu yang diinginkan: \n")
        if (user_input == "1" and isLogged):
            if(getRole(user[4]) == 'admin'):
                register()
                input("Registrasi sudah berhasil ^_^")
            else:
                input("Access Denied. Press any key to continue...")
        elif (user_input == "2"):
            if isLogged:
                input("Anda sudah login!...")
            else:
                isLogged, user = login()
        elif (user_input == "11" and isLogged):
            search_game_at_store()
            input("Press any key to continue...")
        elif(user_input == "13"):
            Help()
            input("Press any key to continue...")
        elif(not(isLogged)):
            input(
                "Ara ara~, Sepertinya kamu belum login. Mohon login terlebih dahulu...")
        else:
            input(
                "Hmm, Command sepertinya tidak dapat ditemukan atau tidak valid. Silahkan coba kembali...")
