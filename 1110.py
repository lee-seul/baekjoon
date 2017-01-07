# coding: utf-8

def plus(n):
    if n < 10:
        tmp = n%10
    else:
        tmp = n//10 + n%10 
    return int(str(n%10) +str(tmp%10))

n = int(input())

cnt = 1
tmp = plus(n)
while True:
    if n == tmp:
        break
    tmp = plus(tmp)
    cnt+=1

print(cnt)
