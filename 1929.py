# coding: utf-8

import sys
write = sys.stdout.write
read = sys.stdin.readline

m, n = map(int, read().split())

def sieve(n, m):
    if n < 2:
        return []
    s = [0, 0] + [1] * (n-1)
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            s[i*2::i] = [0] * ((n-i)//i)
    return [i for i, v in enumerate(s) if v and i >= m]

result = sieve(n, m)

for i in result:
    write(str(i)+"\n") 


