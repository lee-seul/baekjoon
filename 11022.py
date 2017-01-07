# coding: utf-8

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i+1, a, b, a+b))
