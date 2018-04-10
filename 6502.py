# coding: utf-8


i = 1
while True:
    numbers = list(map(int, input().split()))
    if len(numbers) == 1 and numbers[0] == 0:
        break
    
    r, w, l = numbers
    result = 'fits on the table.'
    if pow(r*2, 2) < pow(w, 2) + pow(l, 2):
        result = 'does not fit on the table.'

    print('Pizza {} {}'.format(i, result))
    i += 1

