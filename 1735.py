# coding: utf-8

def gcd(a, b):
    if not a % b:
        return b
    return gcd(b, a % b)

c1, p1 = map(int, input().split())
c2, p2 = map(int, input().split())

num = gcd(p1, p2)

c1 *= p2//num
c2 *= p1//num
p1 *= p2//num

c1 += c2

num = gcd(p1, c1)

c1 //= num
p1 //= num

print(c1, p1)

