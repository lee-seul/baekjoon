# coding: utf-8

def gcd(a, b):
    if not a % b:
        return b
    return gcd(b, a%b)


n = int(input())
radius = list(map(int, input().split()))

for i in range(1, n):
    gcd_value = gcd(radius[0], radius[i])
    radius[i] = "{}/{}".format(radius[0]//gcd_value, 
                               radius[i]//gcd_value) 

for i in range(1, n):
    print(radius[i])

