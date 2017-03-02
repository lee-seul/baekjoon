# coding: utf-8

l = [[0 for j in range(101)] for i in range(101)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            l[x+i][y+j] = 1

result = 0
for e in l:
    result += e.count(1)

print(result)


