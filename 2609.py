# coding: utf-8

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

def lcm(a,b):
    return int(a*b/gcd(a, b))

a, b = map(int, input().split())

print(gcd(max(a, b), min(a, b)))
print(lcm(max(a, b), min(a, b)))

