# coding: utf-8

def fibonacci(n):
    a, b, tmp = 0, 1, 0
    for _ in range(n):
        tmp = a + b
        a = b
        b = tmp
    print(a)
        
fibonacci(int(input()))

