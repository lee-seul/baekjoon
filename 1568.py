# coding: utf-8


n = int(input())

number = 1
cnt = 0
while n:
    if n >= number:
        n -= number
        number += 1
        cnt += 1
    else:
        number = 1

print(cnt)

