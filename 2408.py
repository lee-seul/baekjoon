# coding: utf-8


n = int(input())

ex = ''
for _ in range(2*n-1):
    s = input()
    if s == '/':
        s = '//'
    ex += s

print(eval(ex))
