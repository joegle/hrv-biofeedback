import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import date2num
import matplotlib.cbook as cbook
from matplotlib.ticker import MaxNLocator

f=open("files.txt","r")
dates=[]
for line in f.readlines():
    date_object = datetime.datetime.strptime(line, '%Y-%m-%d-%H:%M:%S.txt\n')
    dates.append(date_object)

dates = np.array(dates)
fig, ax = plt.subplots()

plt.hist(date2num(dates), 50, normed=0, facecolor='green', alpha=0.75)

years    = mdates.YearLocator()   # every year
months   = mdates.MonthLocator()  # every month
monthsFmt = mdates.DateFormatter('%b')
yearsFmt = mdates.DateFormatter('%Y')

#plt.plot(dates,'bo')

ax.xaxis.set_minor_locator(months)
ax.xaxis.set_minor_formatter(monthsFmt)
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
#ax.xaxis.set_minor_locator(MaxNLocator(10,prune='upper'))

datemin = datetime.date(dates.min().year, 1, 1)
datemax = datetime.date(dates.max().year,dates.max().month+1, 1)
ax.set_xlim(datemin, datemax)

plt.grid(True)

#fig.autofmt_xdate()
#plt.gcf().autofmt_xdate()

ax.xaxis.set_tick_params(which='major', pad=15)

plt.title("Recording Activity")
plt.ylabel("Number of Sessions")
plt.xlabel("Date")
plt.show()
