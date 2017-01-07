#coding: utf-8

mon = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

m, d = map(int, input().split())
for i in range(m):
    d += day[i]

print(mon[d%7])

