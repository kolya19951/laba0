import csv
# import pandas as pd

# NYZHNYK, NAZARII, #11,

k = 1                #порядковий номер другої літери імені (A = 1)
n = (25 % 12) + 1      #залишок від ділення другої летери прізвища(Y = 25) на 12   +1
y = 11 + 1996 #сума порядкового номеру у групі та числа 1996
m = 12 - n + 1
z = 2015 - 11 #різниця 2015 - порядковий номер у групі

countRainyDays = 0

with open('weather_madrid_LEMD_1997_2015.csv', 'r+') as myFile:
    reader = csv.reader(myFile)

    for i in range(0, k + 4 + 1):    # +1 for adding header
        line = myFile.readline()
        print(line)



print(countRainyDays)


myFile.close()