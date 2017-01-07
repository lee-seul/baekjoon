# coding: utf-8

n = int(input())
result = 0
if n % 5 == 0:
    result = n // 5
else:
    while n % 5 != 0 and n >= 3:
        n -= 3
        result += 1
    if n != 0 and n % 5 == 0:
        result += n // 5
    elif n != 0 or result == 0:
        result = -1
    
print(result)
