# coding: utf-8

n = int(input())

cups = [1, 0, 0]
for _ in range(n):
    x, y = map(int, input().split())
    temp = cups[x-1]
    cups[x-1] = cups[y-1]
    cups[y-1] = temp

for i in range(3):
    if cups[i]:
        print(i+1)

