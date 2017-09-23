import csv
import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# import pandas as pd

# Symotiuk, Mykola, #13,

k = 25  # порядковий номер другої літери імені (A = 1)
n = (25 % 12) + 1  # залишок від ділення другої летери прізвища(Y = 25) на 12   +1
y = 13 + 1996  # сума порядкового номеру у групі та числа 1996
m = 12 - n + 1
#m = 12
z = 2015 - 13  # різниця 2015 - порядковий номер у групі
#z = 2015
l = []
maxHumidity = 0
daysHumidity = 0
xlist = []
ylist = []
zlist = []

countRainyDays = 0

def f_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xlist, ylist, color='red', linewidth=1, label='4a')
    ax.plot(xlist, zlist, color='blue', linewidth=1, label='4b')

    ax.grid(True)
    ax.legend()
    plt.show()

with open('weather_madrid_LEMD_1997_2015.csv', 'r+') as myFile:
    reader = csv.reader(myFile)
    next(reader)
    for line in myFile:
        l.append(line.split(','));
        # l.append(datetime.datetime.strptime(line[:line.find(',')], "%Y-%m-%d"))
        # if ((l[len(l) - 1].year == y) & (l[len(l) - 1].month == n) & (line.find('Rain') != -1)):
        # countRainyDays += 1
        # for i in myFile:  # +1 for adding header
        #     line = myFile.readline()
        #     l.append(datetime.datetime.strptime(line[:line.find(',')], "%Y-%m-%d"))
        #     print(line)
        #     if ((l[len(l) - 1].year == y) & (l[len(l) - 1].month == n)):
        #         print(l[len(l) - 1])
        #         print(line + 'success')
    for i in range(0, len(l) - 1):
        l[i][0] = datetime.datetime.strptime(l[i][0], "%Y-%m-%d")
        if ((l[i][0].year == y) & (l[i][0].month == n) & (l[i][21].find('Rain') != -1)):
            countRainyDays += 1
        if ((l[i][0].year == z) & (l[i][0].day == n)):
            maxHumidity += float(l[i][7])
            daysHumidity += 1
        if ((l[i][0].year == z) & (l[i][0].month == m)):
            xlist.append(l[i][0].day)
            ylist.append(float(l[i][1]) - float(l[i][3]))
            zlist.append(float(l[i][19]))



print('Кількисть днів коли йшов дощ ' + str(n) + ' місяця ' + str(y) + ' року: ' + str(countRainyDays))
print('Середня максимальна вологість ' + str(n) + ' місяця ' + str(y) + ' року: ' + str(maxHumidity/daysHumidity))

f_plot()


myFile.close()




# Пример функции с объединением и в кортеж args и в словарь **kwargs

# range(0, k + 4 + 1)
# 7
