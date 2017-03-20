# coding: utf-8

n = int(input())
values = []
for _ in range(n):
    value = int(input())
    values.append(value)

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

