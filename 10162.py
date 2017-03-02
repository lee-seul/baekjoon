# coding: utf-8

t = int(input())

if t % 10:
    print(-1)
else:
    print(t//300, (t % 300)//60, (t % 60)//10)


