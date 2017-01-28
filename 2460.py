# coding: utf-8

max_value = 0
count = 0
for _ in range(10):
    off, on = map(int, input().split())
    count -= off
    count += on
    if max_value < count:
        max_value = count

print(max_value)
