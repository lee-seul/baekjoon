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
    if m == x and n != y:
        x = 0
    if m != x and n == y:
        y = 0
    if m == x and n == y:
        result = ma
    else:
        tmp = [x+m*i for i in range(ma//m+1) if x+m*i == ma or x+m*i % m == x]
        for e in tmp:
            if e % n == y and e % m == x:
                result = e
                break
    print(result)
