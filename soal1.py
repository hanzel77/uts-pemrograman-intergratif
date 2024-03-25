# Nama: Hanzel Oclihar Tjiam
# NIM: 221402064

# Soal 1

import datetime as datetime
import calendar


days_in_a_year = 365 + calendar.isleap(datetime.datetime.now().year)
x = int(input("Enter a whole number: "))


result = (x / days_in_a_year)

print('{0:8.11f}'.format(result))





