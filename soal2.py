# Nama: Hanzel Oclihar Tjiam
# NIM: 221402064

# Soal 2

import datetime as datetime

day = datetime.datetime.now().date().day
result = 1

for i in range(1, day + 1):
    result *= i

print(result)
