# coding: utf-8 


n = int(input())

for _ in range(n):
    s = input().split(' = ')
    temp = eval(s[0])
    if temp == int(s[1]):
        print('correct')
    else:
        print('wrong answer')

