from package import *

tmp = []
for i in range(length(user)):
    addObj(tmp, ';'.join(user[i]))
    addObj(tmp, '\n')
print(''.join(tmp))
