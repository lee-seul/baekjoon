# coding: utf-8


n = int(input())
k = int(input())

result = n
for _ in range(k):
    n = int(str(n) + '0')
    result += n

print(result)
