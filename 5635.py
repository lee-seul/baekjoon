# coding: utf-8

def year(dd, mm, yy):
    yy = (2017 - yy) * 365
    mm = (12 - mm) * 30
    dd = (30 - dd)
    return yy + mm + dd

n = int(input())

years = []
for _ in range(n):
    name, d, m, y = input().split()
    d = year(int(d), int(m), int(y))
    years.append((d, name))

years.sort()
print(years[0][1])
print(years[-1][1])
