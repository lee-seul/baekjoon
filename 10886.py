# coding: utf-8

n = int(input())

c = 0
nc = 0

for _ in range(n):
    a = int(input())
    if a:
        c += 1
    else:
        nc += 1
if c > nc:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
