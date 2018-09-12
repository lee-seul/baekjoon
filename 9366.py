# coding: utf-8


n = int(input())

for i in range(n):
    numbers = [int(x) for x in input().split()]
    numbers.sort()
    
    if numbers[0] + numbers[1] <= numbers[2]:
        result = 'invalid!'
    else:
        numbers = set(numbers)
        if len(numbers) == 1:
            result = 'equilateral'
        if len(numbers) == 2:
            result = 'isosceles'
        if len(numbers) == 3:
            result = 'scalene'
    print('Case #{}: {}'.format(i+1, result))
