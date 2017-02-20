# coding: utf-8

n = int(input())

max_num = 0
for _ in range(n):
    temp = 0
    numbers = list(map(int, input().split()))
    if len(set(numbers)) == 1:
        temp = 10000 + numbers[0] * 1000
    elif len(set(numbers)) == 2:
        numbers.sort()
        temp = 1000 + numbers[1] * 100
    else:
        temp = max(numbers) * 100

    if max_num < temp:
        max_num = temp

print(max_num)

