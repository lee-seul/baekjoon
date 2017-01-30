# coding: utf-8

def fac(num):
    result = 1
    for i in range(2, num+1):
        result *= i
    return result

while True:
    n = int(input())
    if not n:
        break
    result = 0
    n = list(str(n))
    i = 1
    while n:
        result += int(n.pop()) * fac(i)
        i += 1
    print(result)
        
