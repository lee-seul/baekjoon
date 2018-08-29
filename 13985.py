# coding: utf-8


s = input().split('=')
if eval(s[0]) == int(s[1]):
    print('YES')
else:
    print('NO')
