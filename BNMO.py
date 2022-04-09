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

        # Main Menu
        printMenu()

        # Choose Menu
        user_input = input("Silahkan pilih menu yang diinginkan: \n")
        if (user_input == "1" and isLogged):  # Register
            if(role == 'admin'):
                register(user)
            else:
                input("Access Denied. Press any key to continue...")
        elif (user_input == "2"):  # Login
            if isLogged:
                input("Anda sudah login!...")
            else:
                isLogged, current_id, current_username = login(user)
                role = getRole(user, current_id)
        elif(user_input == "3" and isLogged):  # Tambah Game
            if(role == 'admin'):
                tambah_game(game)
            else:
                input("Access Denied. Press any key to continue...")
        elif(user_input == "4" and isLogged):
            if(role == 'admin'):
                ubah_game(game)
            else:
                input("Access Denied. Press any key to continue...")
        elif(user_input == "5" and isLogged):
            if(role == 'admin'):
                ubah_stok(game)
            else:
                input("Access Denied. Press any key to continue...")
        elif(user_input == "6" and isLogged):
            list_game_toko(game)
        elif(user_input == "7" and isLogged):
            if(role == 'user'):
                buy_game(current_id, user, game, kepemilikan, riwayat)
            else:
                input("Access Denied. Press any key to continue...")
        elif(user_input == "8" and isLogged):
            if(role == 'user'):
                list_game(current_id, game, kepemilikan)
            else:
                input("Access Denied. Press any key to continue...")
        elif(user_input == "9" and isLogged):
            if(role == 'user'):
                search_my_game(current_id, game, kepemilikan)
            else:
                input("Access Denied. Press any key to continue...")
        elif (user_input == "10" and isLogged):
            search_game_at_store(game)
        elif(user_input == "11" and isLogged):
            if(role == 'admin'):
                topup(user)
            else:
                input("Access Denied. Press any key to continue...")
        elif(user_input == "12" and isLogged):
            if(role == 'user'):
                history(current_id, riwayat)
            else:
                input("Access Denied. Press any key to continue...")
        elif(user_input == "13"):  # Help
            if isLogged == False:
                Help('user')
            elif role == 'admin':
                Help('admin')
            else:
                Help('user')
            input("Press any key to continue...")
        elif(user_input == "14" and isLogged):  # Save Program
            save(user, game, kepemilikan, riwayat)
        elif(user_input == "15"):  # Exit Program
            exit_program(user, game, kepemilikan, riwayat)
            break
        elif(not(isLogged)):  # Not Logged in State
            input(
                "Ara ara~, Sepertinya kamu belum login. Mohon login terlebih dahulu...")
        else:  # Input is not valid
            input(
                "Hmm, Command sepertinya tidak dapat ditemukan atau tidak valid. Silahkan coba kembali...")
