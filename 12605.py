# coding: utf-8

n = int(input())

casese = []
for _ in range(n):
    l = input().split()
    l.reverse()
    casese.append(l)

for i, string in enumerate(casese):
    string = ' '.join(string)
    result = 'Case #{}: {}'.format(i+1, string)
    print(result)

