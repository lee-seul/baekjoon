# coding: utf-8

n = int(input())

dp = [0 for _ in range(n+1)]
dp[0] = 1
if n >= 2:
    dp[2] = 3

for i in range(3, n+1):
    dp[i] = 3 * dp[i-2]
    x = 4
    while i - x >= 0:
        dp[i] += 2 * dp[i-x]
        x += 2

print(dp[n])
        
