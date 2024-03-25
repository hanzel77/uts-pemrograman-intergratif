# Nama: Hanzel Oclihar Tjiam
# NIM: 221402064

# Soal 3

import datetime as datetime

x = int(input("Enter a number: "))

now = datetime.datetime.now()

result = now + datetime.timedelta(days = x)

print(result.strftime("%A on %d %B %Y"))



