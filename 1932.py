# coding: utf-8

n = int(input())
l = []

for _ in range(n):
    l.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(l[i-1])-1):
        if j == 0 or l[i-1][j] >= l[i-1][j-1]:
            l[i][j] += l[i-1][j]
        if l[i-1][j] > l[i-1][j+1]:
            l[i][j+1] += l[i-1][j]
    if l[i-1][len(l[i-1])-1] >= l[i-1][len(l[i-1])-2]:
        l[i][len(l[i-1])-1] += l[i-1][len(l[i-1])-1]
    l[i][len(l[i-1])] += l[i-1][len(l[i-1])-1]

print(max(l[n-1]))
