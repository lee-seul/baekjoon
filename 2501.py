# coding: utf-8

n, k = map(int, input().split())

result = 0
cnt = 0
for i in range(1, n+1):
    if not n % i:
        cnt += 1
    if cnt == k:
        result = i
        break

print(result)
