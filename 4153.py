# coding: utf-8 


while True:
    numbers = list(map(int, input().split()))
    numbers.sort()

    a, b, c = numbers
    if not a and not b and not c:
        break 

    result = a ** 2 + b ** 2 == c ** 2
    if result:
        print('right')
    else:
        print('wrong')
