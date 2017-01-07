# coding: utf-8

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

def lcm(a, b):
    return int(a*b/gcd(a,b))

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    result = -1
    ma = lcm(m, n)
    p = x
    while p <= ma:
        if p % n == y and p % m == x:
            result = p
            break
        p += m
    print(result) 
