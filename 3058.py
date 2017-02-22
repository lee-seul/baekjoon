# coding: utf-8

t = int(input())

for _ in range(t):
    numbers = list(map(int, input().split()))
    even = [x for x in numbers if not x % 2]
    even.sort()
    print(sum(even), even[0])

