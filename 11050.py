# coding: utf-8

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

n, k = map(int, input().split())
print(factorial(n)//(factorial(k)*factorial(n-k)))
