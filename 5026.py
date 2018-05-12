# coding: utf-8


n = int(input())

for _ in range(n):
    s = input()
    if s == 'P=NP':
        print('skipped')
        continue
    print(eval(s))
