from code.base import *

global user, game, kepemilikan, riwayat

# ArgParser
parser = argparse.ArgumentParser(description='Read lines from CLI')
parser.add_argument('FolderName', type=str, help='Folder Name')
args = parser.parse_args()
dir = args.FolderName

# CSV to Array
user = csv_to_mat("user")
game = csv_to_mat("game")
kepemilikan = csv_to_mat("kepemilikan")
riwayat = csv_to_mat("riwayat")
