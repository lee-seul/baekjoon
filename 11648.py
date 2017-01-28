# coding: utf-8

def mul(num):
    result = 1
    for s in num:
        result *= int(s)
    return str(result)

n = input()

cnt = 0
while len(n) > 1:
    n = mul(n)
    cnt += 1

print(cnt)
