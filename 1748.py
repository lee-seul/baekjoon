# coding: utf-8

n = int(input())
cnt = len(str(n))

tmp = 0; result = 0
for i in range(cnt, 0, -1):
    tmp = n
    if i > 1:
        n = n - 10**(i-1) + 1
    result += n * i
    n = tmp - n
print(result)

