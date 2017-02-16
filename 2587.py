# coding: utf-8

values = []
for _ in range(5):
    value = int(input())
    values.append(value)

values.sort()
print(sum(values)//5)
print(values[2])

