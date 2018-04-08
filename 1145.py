# coding: utf-8


numbers = list(map(int, input().split()))
numbers.sort()

start = numbers[0] - 1
NOT_FOUND = True
while NOT_FOUND:
    count = 0
    start += 1
    for number in numbers:
        if not start % number:
            count += 1
        if count == 3:
            NOT_FOUND = False
            break 

print(start)
