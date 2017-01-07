# coding: utf-8

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return str(result)

fac = factorial(int(input()))
fac = list(fac)
fac.reverse()
result = 0
for i in range(len(fac)):
    if fac[i] == '0':
        result += 1
    else:
        break
print(result)


