# global user, game, kepemilikan, riwayat
# user = [''for i in range(1000)]
# game = [''for i in range(1000)]
# kepemilikan = [''for i in range(1000)]
# riwayat = [''for i in range(1000)]


# def spliter(line, delimiter):
#     arr = []
#     tmp = ''
#     for c in line:
#         if c == delimiter:
#             arr.append(tmp)
#             tmp = ''
#         elif c == "\n":
#             break
#         else:
#             tmp += c
#     return arr


# # CONVERT LINE TO DATA
# csv_to_array = []
# f = open('tes.csv', 'r')
# next(f)
# raw_lines = f.readlines()
# f.close()
# for raw_line in raw_lines:
#     csv_to_array += [spliter(raw_line, ';')]

# print(csv_to_array)

list_data = []
enter = ""
with open("tes.csv", "r") as new_file:
    for line in new_file:
        for element in line:
            if element == ";":
                list_data += [enter]
                enter = ""
            elif element == "\n":
                list_data += [enter]
                break
            else:
                enter += element
    print(list_data)
