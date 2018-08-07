# coding: utf-8


import math


n = input()
a = list(map(int, input().split()))

g = a[0]
gcd = lambda x,y:x if not y else gcd(y,x%y)

for i in a:
    g=gcd(g,i)

x = int(math.sqrt(g))

ans=[]
for i in range(1,x+1):
    if g % i > 0:
        continue
    
    ans.append(i)
    if i != g / i:
        ans.append(int(g/i))

ans.sort()
for i in ans:
    print(i)
