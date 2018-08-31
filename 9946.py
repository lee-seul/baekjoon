# coding: utf-8 

cnt = 1
while True:
    a = input()
    b = input()
    if a == 'END' and b == 'END':
        break

    a = sorted(list(a))
    b = sorted(list(b))
    result = 'different'
    if a == b:
        result = 'same'

    print('Case {}: {}'.format(cnt, result))
    cnt += 1
     
