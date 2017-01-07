# coding: utf-8

def d(n):
    result = n
    for i in str(n):
        result += int(i)
    return result

l = []
for i in range(1, 10001):
    l.append(d(i))

for i in range(1, 10001):
    if i not in l:
        print(i)


