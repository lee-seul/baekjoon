# coding: utf-8

a = list(input())
b = list(input())

result = 0
for i in range(97, 123):
    result += abs(a.count(chr(i)) - b.count(chr(i)))

print(result)
