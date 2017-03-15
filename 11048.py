# coding: utf-8

n, m = map(int, input().split())
candy = []

for _ in range(n):
    c = list(map(int, input().split()))
    candy.append(c)

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +\
        candy[i-1][j-1]

print(dp[n][m])

