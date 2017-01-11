# coding: utf-8

max_value = 0
value = 0
for _ in range(4):
    off, on = map(int, input().split())
    value -= off
    value += on
    if value > max_value:
        max_value = value
print(max_value)
