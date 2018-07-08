# coding: utf-8


numbers = list(map(int, input().split()))
numbers.sort()
gap = numbers[1] - numbers[0]
gap2 = numbers[2] - numbers[1]

if not gap == gap2:
    if gap > gap2:
        print(numbers[0] + gap2)
    else:
        print(numbers[1] + gap)
else:
    print(numbers[2] + gap)

