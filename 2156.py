# coding: utf-8

n = int(input())
wine = []

for _ in range(n):
    w = int(input())
    wine.append(w)


dp = [[0 for _ in range(3)] for _ in range(n+1)]
dp[1][1] = wine[0]
dp[1][2] = wine[0]

for i in range(2, n+1):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + wine[i-1]
    dp[i][2] = dp[i-1][1] + wine[i-1]

print(max(dp[n]))

