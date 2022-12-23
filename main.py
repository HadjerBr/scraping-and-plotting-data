# plotting the data using matplotlib

import pandas as pd
from matplotlib import pyplot as plt
import csv
import SCRAPING


SCRAPING.scraping()

a = []
b = []

with open('files/jobs_salaries.csv','r') as file:
    plots = csv.reader(file, delimiter = ',')
    next(plots)
    for row in plots:
        a.append(row[0])
        b.append(int(row[1].replace(".", "")))
file.close()

plt.bar(a, b, width = 0.72, label = "Ortalama Maas")
plt.xlabel('Isler')
plt.ylabel('Yillik Ortalama Maaslar(TL)')
plt.title('Bilgisayar Bilimleri Islerin Ortalama Maaslari')
plt.legend()
# plt.show()

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)


x = []
y = []

x1 = []
y1 = []

x2 = []
y2 = []

x3 = []
y3 = []


with open('files/Bilgisayar Mühendisi_most_hired_fields.csv','r') as file:
    plots = csv.reader(file, delimiter = ',')
    next(plots)
    for row in plots:
        x.append(row[0])
        y.append(int(float(row[1].replace(',', '').replace('%', ''))))
file.close()


with open('files/Mobil Yazılım Mühendisi_most_hired_fields.csv','r') as file:
    plots = csv.reader(file, delimiter = ',')
    next(plots)
    for row in plots:
        x1.append(row[0])
        y1.append(int(float(row[1].replace(',', '').replace('%', ''))))
file.close()

with open('files/Veri Bilimci_most_hired_fields.csv','r') as file:
    plots = csv.reader(file, delimiter = ',')
    next(plots)
    for row in plots:
        x2.append(row[0])
        y2.append(int(float(row[1].replace(',', '').replace('%', ''))))
file.close()

with open('files/Yazılım Mühendisi_most_hired_fields.csv','r') as file:
    plots = csv.reader(file, delimiter = ',')
    next(plots)
    for row in plots:
        x3.append(row[0])
        y3.append(int(float(row[1].replace(',', '').replace('%', ''))))
file.close()


colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
patches, texts = ax1.pie(y, colors=colors, shadow=True, startangle=90)
patches1, texts1 = ax2.pie(y1, colors=colors, shadow=True, startangle=90)
patches2, texts2 = ax3.pie(y2, colors=colors, shadow=True, startangle=90)
patches3, texts3 = ax4.pie(y3, colors=colors, shadow=True, startangle=90)
ax1.set_title("Bilgisayar Mühendisi pozisyonunda most hired 5 fields")
ax1.legend(patches, x, loc="best")
ax2.set_title("Mobil Yazılım Mühendisi pozisyonunda most hired 5 fields")
ax2.legend(patches1, x1, loc="best")
ax3.set_title("Veri Bilimci pozisyonunda most hired 5 fields")
ax3.legend(patches2, x2, loc="best")
ax4.set_title("Yazılım Mühendisi pozisyonunda most hired 5 fields")
ax4.legend(patches3, x3, loc="best")
plt.show()
plt.show()
  
