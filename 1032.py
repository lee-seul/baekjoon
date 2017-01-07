# coding: utf-8

n = int(input())

string = []
for _ in range(n):
    string.append(input())
    
length = len(string[0])
l = [0 for i in range(length)]

for i in range(length):
    std = string[0][i]
    for s in string:
        if std != s[i]:
            l[i] = 0
            break
        l[i] = 1

result = ""
for i in range(length):
    if l[i] == 0:
        result += "?"
    else:
        result += string[0][i]

print(result)


