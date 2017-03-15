# coding: utf-8

n = int(input())
result = [[0 for _ in range(10)] for _ in range(n+1)]
for i in range(1, 10):
    result[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j-1 >= 0:
            result[i][j] += result[i-1][j-1]
        if j+1 <= 9:
            result[i][j] += result[i-1][j+1]

ans = 0
for i in range(10):
    ans += result[n][i]

print(ans%1000000000)

