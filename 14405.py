# coding: utf-8


s = input()

s = s.replace('pi', ' ').replace('ka', ' ').replace('chu', ' ')
s = s.replace(' ', '')
if not s:
    print('YES')
else:
    print('NO')
