# coding: utf-8

record = []
while True:
    temper = float(input())
    if temper == 999:
        break
    record.append(temper)
    if len(record) > 1:
        print("{:.2f}".format(record[-1] - record[-2]))

