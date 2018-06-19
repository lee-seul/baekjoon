# coding: utf-8 


data = []
for _ in range(5):
    n = int(input())
    data.append(n)

result = 0

if data[0] < 0:
    first = 0 - data[0]
    result += first * data[2]
    result += data[3]
    result += data[1] * data[4]

if data[0] > 0:
    first = data[1] - data[0]
    result = first * data[4]

print(result)

