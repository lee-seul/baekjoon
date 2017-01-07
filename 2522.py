# coding: utf-8

n = int(input())

i = 0
for j in range(2*n-1):
    if j < n:
        i += 1
    else:
        i -= 1
    s = "*" * i
    print(s.rjust(n))


