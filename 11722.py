# coding: utf-8

n = int(input())
a = list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

for i in range(0, n):
    dp[i] = 1
    for j in range(i):
        if a[i] < a[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))

