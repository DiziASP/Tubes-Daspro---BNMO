from package import*

if __name__ == "__main__":
    """
        Running the Main Program
    """
    isLogged = False  # Login Status

    # Logged User Data
    current_id = ''
    current_username = ''
    role = ''

    # Loading Sequence
    user, game, kepemilikan, riwayat = load()

    while True:
        os.system('cls')  # Clear Console each time a command has finished

        printMenu()  # Main Menu

        user_input = strip_str(  # Choose Menu
            input("Silahkan pilih menu yang diinginkan: \n>>> "))

        if (user_input.lower() == "register" and isLogged):  # Register
            if(role == 'admin'):
                register(user)
            else:
                input("Access Denied. Press any key to continue...")

        elif (user_input.lower() == "login"):  # Login
            if isLogged:
                input("Anda sudah login!...")
            else:
                isLogged, current_id, current_username = login(user)
                role = getRole(user, current_id)

        elif(user_input.lower() == "tambah_game" and isLogged):  # Tambah Game
            if(role == 'admin'):
                tambah_game(game)
            else:
                input("Access Denied. Press any key to continue...")

        elif(user_input.lower() == "ubah_game" and isLogged):  # Ubah Game
            if(role == 'admin'):
                ubah_game(game)
            else:
                input("Access Denied. Press any key to continue...")

        elif(user_input.lower() == "ubah_stok" and isLogged):  # Ubah Stok
            if(role == 'admin'):
                ubah_stok(game)
            else:
                input("Access Denied. Press any key to continue...")

        elif(user_input.lower() == "list_game_toko" and isLogged):  # List game di Toko
            list_game_toko(game)

        elif(user_input.lower() == "buy_game" and isLogged):  # Buy Game
            if(role == 'user'):
                buy_game(current_id, user, game, kepemilikan, riwayat)
            else:
                input("Access Denied. Press any key to continue...")

        elif(user_input.lower() == "list_game" and isLogged):  # List Game
            if(role == 'user'):
                list_game(current_id, game, kepemilikan)
            else:
                input("Access Denied. Press any key to continue...")

        elif(user_input.lower() == "search_my_game" and isLogged):  # Search User Game
            if(role == 'user'):
                search_my_game(current_id, game, kepemilikan)
            else:
                input("Access Denied. Press any key to continue...")

        elif (user_input.lower() == "search_game_at_store" and isLogged):  # Search Game At Store
            search_game_at_store(game)

        elif(user_input.lower() == "topup" and isLogged):  # Topup Saldo User
            if(role == 'admin'):
                topup(user)
            else:
                input("Access Denied. Press any key to continue...")

        elif(user_input.lower() == "riwayat" and isLogged):  # Riwayat User
            if(role == 'user'):
                history(current_id, riwayat)
            else:
                input("Access Denied. Press any key to continue...")

        elif(user_input.lower() == "help"):  # Help
            if isLogged == False:
                Help('')
            elif role == 'admin':
                Help('admin')
            else:
                Help('user')
            input("Press any key to continue...")

        elif(user_input.lower() == "save" and isLogged):  # Save Program
            save(user, game, kepemilikan, riwayat)

        elif(user_input.lower() == "exit"):  # Exit Program
            exit_program(user, game, kepemilikan, riwayat)
            break

        elif(user_input.lower() == "kerangajaib"):  # Magic Conch Shell
            kerangajaib()
            input("Press any key to continue...")

        elif(user_input.lower() == "tictactoe"):  # Tictactoe
            tictactoe()
            input("Press any key to continue...")

        elif(not(isLogged)):  # Not Logged in State
            input(
                "Ara ara~, Sepertinya kamu belum login. Mohon login terlebih dahulu...")

        else:  # Input is not valid
            input(
                "Hmm, Command sepertinya tidak dapat ditemukan atau tidak valid. Silahkan coba kembali...")
