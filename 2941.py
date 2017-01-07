# coding: utf-8


cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

string = input()
result = 0

i = 0 
while len(string) > i:
    if string[i:i+2] in cro:
        result += 1
        i += 2
    elif string[i:i+3] in cro:
        result += 1
        i += 3
    else:
        i += 1
        result += 1

print(result)
