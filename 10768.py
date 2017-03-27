# coding: utf-8

month = int(input())
day = int(input())

month *= 100
month += day

if month > 218:
    print("After")
elif month == 218:
    print("Special")
else:
    print("Before")

