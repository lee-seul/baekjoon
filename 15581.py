# coding: utf-8


n = int(input())
string = input()

idx = 0
count = 0
while idx < n:
    if not string[idx] == 'p':
        idx += 1
        continue
    
    if string[idx:idx+4] == 'pPAp':
        count += 1
        idx += 4
    else:
        idx += 1

print(count)

