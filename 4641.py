# coding: utf-8


while True:
    numbers = list(map(int, input().split()))
    if len(numbers) == 1 and numbers[0] == -1:
        break
    numbers = numbers[:-1]
    count = 0
    for x in numbers:
        for y in numbers:
            if y == x:
                continue
            if x * 2 == y:
                count += 1
    print(count)

