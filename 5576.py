# coding: utf-8

w = []
k = []

for i in range(20):
    score = int(input())
    if i < 10:
        w.append(score)
    else:
        k.append(score)

w.sort()
k.sort()

print(sum(w[7:]), sum(k[7:]))


