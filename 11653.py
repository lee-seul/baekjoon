# coding: utf-8

import sys
write = sys.stdout.write
result = []

n = int(input())

i = 2
while n != 1:
    if not n % i:
        result.append(i)
        n /= i
    else:
        i += 1

for e in result:
    write("{}\n".format(e))
    
