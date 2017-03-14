# coding: utf-8

def gcd(a, b):
    if not a % b:
        return b
    return gcd(b, a%b)

def lcm(a, b):
    return int(a*b/gcd(a, b))

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    print(lcm(x, y), gcd(x, y))

