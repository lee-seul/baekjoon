# coding: utf-8

while True:
    numbers = list(map(int, input().split()))
    numbers.sort()
    set_num = set(numbers)
    if len(set_num) == 1 and set_num == {0}:
        break

    if numbers[0] + numbers[1] <= numbers[2]:
        print('Invalid')
        
    else:
        if len(set_num) == 1:
            print('Equilateral')
        if len(set_num) == 2:
            print('Isosceles')
        if len(set_num) == 3:
            print('Scalene')
