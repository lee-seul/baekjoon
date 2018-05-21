# coding: utf-8


char = {chr(n): 0 for n in range(65, 91)}

s = input().upper()

for c in s:
    if c in char:
        char[c] += 1


for i in range(65, 91):
    key = chr(i)
    print('{} | {}'.format(key, '*' * char[key]))

