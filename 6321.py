# coding: utf-8

def com_name(string):
    result = []
    for c in string:
        if c == 'Z':
            result.append('A')
        else:
            result.append(chr(ord(c)+1))
    print("".join(result))

n = int(input())

names = []
for i in range(n):
    s = input()
    names.append(s)

for i in range(n):
    print("String #{}".format(i+1))
    com_name(names[i])
    if i != n-1:
        print()
