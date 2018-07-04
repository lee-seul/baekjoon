# coding: utf-8 


def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)


a, b = map(int, input().split())

t = gcd(a, b)
print('1' * t)

