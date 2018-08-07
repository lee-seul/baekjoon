# coding: utf-8

a, b = map(int, input().split())

numbers = []
num = 1
while len(numbers) < 1000:
    numbers.extend([num] * num)
    num += 1

numbers = numbers[:1000]
print(sum(numbers[a-1:b]))
