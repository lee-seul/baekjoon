# coding: utf-8


n = int(input())

n = list(bin(n))

result = 0
for i in range(2, len(n)):
    digit = 2 ** (i-2)
    result += int(n[i]) * digit 

print(result)

