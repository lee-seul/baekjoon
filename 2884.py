# coding: utf-8

h, m = map(int, input().split())

if m < 45:
    h = (h - 1) % 24
    
m = (m - 45) % 60

print(h, m)

