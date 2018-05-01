# coding: utf-8


n = int(input())

numbers = list(map(int, input().split()))

count = 0
for i, number in enumerate(numbers):
    if not number == i + 1:
        count += 1

print(count)
