import csv
import datetime

# import pandas as pd

# Symotiuk, Mykola, #13,

k = 25  # порядковий номер другої літери імені (A = 1)
n = (25 % 12) + 1  # залишок від ділення другої летери прізвища(Y = 25) на 12   +1
y = 13 + 1996  # сума порядкового номеру у групі та числа 1996
m = 12 - n + 1
z = 2015 - 13  # різниця 2015 - порядковий номер у групі
l = []

countRainyDays = 0

with open('weather_madrid_LEMD_1997_2015.csv', 'r+') as myFile:
    reader = csv.reader(myFile)
    next(reader)
    for line in myFile:
        l.append(datetime.datetime.strptime(line[:line.find(',')], "%Y-%m-%d"))
        if ((l[len(l) - 1].year == y) & (l[len(l) - 1].month == n) & (line.find('Rain') != -1)):
            countRainyDays += 1
            # for i in myFile:  # +1 for adding header
            #     line = myFile.readline()
            #     l.append(datetime.datetime.strptime(line[:line.find(',')], "%Y-%m-%d"))
            #     print(line)
            #     if ((l[len(l) - 1].year == y) & (l[len(l) - 1].month == n)):
            #         print(l[len(l) - 1])
            #         print(line + 'success')

print(countRainyDays)

myFile.close()

# range(0, k + 4 + 1)
