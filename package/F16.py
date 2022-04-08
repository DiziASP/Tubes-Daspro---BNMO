from .base import*
from .constant import*


def create_folder(folder):
    dir = "./"
    os.chdir(dir)
    if not os.path.exists(folder):
        os.mkdir(folder)


def write_csv(folder, data, string):
    with open(f'./{folder}/{string}.csv', 'w') as f:
        line = ""
        # Looping for every line of data
        for i in range(length(data)):
            # Looping for every item in line
            for j in range(length(data[i])):
                # If item is the last item, doesn't use ;
                if j == length(data[i]) - 1:
                    line += str(data[i][j])
                else:
                    line += f"{data[i][j]};"               # use ;
            line += "\n"                                    # end of line
        f.write(line)
        f.close()


def save():
    user_ = user
    game_ = game
    kepemilikan_ = kepemilikan
    riwayat_ = riwayat

    folder = input("Masukkan nama folder penyimpanan: ")
    create_folder(folder)
    write_csv(folder, user_, "user")
    write_csv(folder, game_, "game")
    write_csv(folder, kepemilikan_, "kepemilikan")
    write_csv(folder, riwayat_, "riwayat")
