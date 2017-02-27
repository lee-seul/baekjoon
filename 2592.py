# coding: utf-8

from collections import Counter

numbers = []

for _ in range(10):
    number = int(input())
    numbers.append(number)
    c = Counter(numbers)
    
print(sum(numbers)//10)
print(c.most_common(1)[0][0])

