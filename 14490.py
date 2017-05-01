# coding: utf-8


def gcd(a, b):
    if not a % b:
        return b
    return gcd(b, a%b)

n, m = map(int, input().split(':'))

g = gcd(n, m)

print("{}:{}".format(n//g, m//g))

