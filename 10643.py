# coding: utf-8


numbers = []
for _ in range(8):
    s = int(input())
    numbers.append(s)

numbers *=2 

m = 0
for i in range(12):
    temp = sum(numbers[i:i+4])
    if temp > m:
        m = temp

print(m)
