# coding: utf-8


n = int(input())
result = 0

for i in range(1, 501):
    value = i ** 2 + n
    if value < (i+1) ** 2:
        break
    if value ** 0.5 == int(value ** 0.5):
        result += 1

print(result)

