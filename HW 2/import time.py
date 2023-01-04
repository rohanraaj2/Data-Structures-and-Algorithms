import time
import csv
deaths = []
activecases = []
d = open("owid-covid-data.csv", "r")
r = csv.reader(d)
n = []
for i in r:
    n.append(i)
d.close()
print (n)

def mergeSort(data):
  l = len(data)
  if l > 1:
    h = l // 2
    f = data[:h]
    s = data[h:]

    mergeSort(f)
    mergeSort(s)

    x = 0
    y = 0
    z = 0

    lof = len(f)
    los = len(s)

    while x < lof and y < los:
      if f[x] < s[y]:
        data[z] = f[x]
        x += 1
      else:
        data[z] = s[y]
        y += 1
      z += 1

    while x < lof:
      data[z] = f[x]
      x += 1
      z += 1
    
    while y < los:
      data[z] = s[y]
      y += 1
      z += 1
