# Nama: Hanzel Oclihar Tjiam
# NIM: 221402064

# Soal 5

import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

f = open(path, "r")

result = 0

for x in f:
    result += int(x)

print("{:,.2f}".format(result))


f.close()