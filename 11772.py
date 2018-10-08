# coding: utf-8


n = int(input())
result = 0
for _ in range(n):
    num = input()
    result += int(num[:-1]) ** int(num[-1])

print(result)
