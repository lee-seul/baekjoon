# coding: utf-8

m = int(input())
n = int(input())

result = []
x = 1
while True:
    num = x ** 2
    if n >= num >= m:
        result.append(num)
    elif num > n:
        break
    x += 1

if len(result):
    print(sum(result))
    print(min(result))
else:
    print(-1)
