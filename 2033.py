# coding: utf-8

n = input()
if len(n) == 1:
    print(n)
else:
    length = len(n)
    n = int(n)
    for i in range(1, length):
        if str(n)[-i] == '5':
            n = int(n) + (10**(i-1))
        n = round(n, -i)
    print(n)
