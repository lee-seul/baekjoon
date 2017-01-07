# coding: utf-8

n = int(input())
l = list(map(int, input().split()))
l.sort()

result = 0; wait = 0
for t in l:
    result += wait + t
    wait += t
print(result)


