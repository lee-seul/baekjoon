# coding: utf-8


t = int(input())

for i in range(t):
    numbers = list(map(int, input().split()))
    numbers.sort()
    a, b, c = numbers
    result = 'no'
    if a ** 2 + b ** 2 == c ** 2:
        result = 'yes'

    print('Scenario #{}:'.format(i+1))
    print(result)
    if i < t - 1:
        print()
