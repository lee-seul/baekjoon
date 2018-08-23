# coding: utf-8


e, f, c = map(int, input().split())

count = (e + f) // c
share = count
remains = (e + f) % c


while True:
    remains += share
    if remains < c:
        break 
    share = remains // c 
    count += share 
    remains %= c

print(count)
