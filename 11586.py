# coding: utf-8

n = int(input())

values = []
for _ in range(n):
    string = list(input())
    values.append(string)

k = int(input())

if k == 2:
    for i in range(n):
        values[i].reverse()

elif k == 3:
    values.reverse()

for i in range(n):
    print("".join(values[i]))
