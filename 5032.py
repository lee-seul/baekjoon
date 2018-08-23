# coding: utf-8


e, f, c = map(int, input().split())


count = 0
remains = 0
share = e + f
while True:
    remains += share
    if remains < c:
        break 
    share = remains // c 
    count += share 
    remains %= c

print(count)
