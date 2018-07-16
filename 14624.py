# coding: utf-8


n = int(input())

if not n % 2:
    print('I LOVE CBNU')
else:
    print('*' * n)
    for i in range(n//2+1):
        empty = ' ' * (((n-1)// 2) - i)
        if not i:
            print(empty + '*')
        else:
            space = ' ' * ((i * 2) - 1)
            print(empty + '*' + space + '*') 
            
