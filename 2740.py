# coding: utf-8

m, n = map(int, input().split())
a = []
b = []
for _ in range(m):
    a.append(list(map(int, input().split())))

n, k = map(int, input().split())
for _ in range(n):
    b.append(list(map(int, input().split())))

result = []
for i in range(m):
    tmp = []
    for j in range(k):
        r = 0
        for l in range(n):
            r += a[i][l] * b[l][j]
        tmp.append(r)
    result.append(tmp)

for i in range(m):
    for j in range(k):
        print(result[i][j], end=" ")
    print()

