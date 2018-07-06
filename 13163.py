# coding: utf-8


n = int(input())

for _ in range(n):
    name = input().split()
    name[0] = 'god'
    print(''.join(name))
