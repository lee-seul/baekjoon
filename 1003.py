# coding: utf-8

from pudb import set_trace
set_trace()

n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))

def fibonacci(n):
    a, b = 1, 0
    tmp = 0
    for _ in range(n):
        tmp = a + b
        a = b
        b = tmp
    print(a, b)

for i in range(n):
    fibonacci(l[i])

