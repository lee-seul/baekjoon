# coding: utf-8

n = int(input())
numbers = list(map(int, input().split()))

result = 0
for i in range(1, min(numbers) + 1):
    for number in numbers:
        if number % i:
            result = 0
            break
        else:
            result = 1
    if result:
        print(i)

