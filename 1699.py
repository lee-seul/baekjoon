# coding: utf-8

from math import sqrt

num = int(input())

dp = [0 for i in range(num+1)]
for i in range(1, num+1):
    for j in range(1, int(sqrt(i))+1):
        if dp[i] > dp[i-j*j] + 1 or not dp[i]:
            dp[i] = dp[i-j*j] +1

print(dp[num])
