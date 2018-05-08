# coding: utf-8 


n = int(input())

cow_dict = {}

result = 0
for _ in range(n):
    c, p = input().split()
    if c in cow_dict and cow_dict[c] != p:
        result += 1
    cow_dict[c] = p

print(result)
