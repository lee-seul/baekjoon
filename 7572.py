# coding: utf-8

t = "ABCDEFGHIJKL"
g = "0123456789"

gapza = []
for i in range(60):
    gapza.append(t[i%12] + g[i%10])

year = int(input())
print(gapza[year%60-4])

