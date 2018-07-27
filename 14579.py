# coding: utf-8 


a, b = map(int, input().split())

base = sum(range(1, a+1))
result = base
for i in range(a, b):
    base += i + 1
    result *= base

print(result % 14579)
    
