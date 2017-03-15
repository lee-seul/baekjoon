# coding: utf-8

s = input()

j = 0
o = 0
for i in range(len(s)-2):
    if s[i:i+3] == "JOI":
        j += 1
    if s[i:i+3] == "IOI":
        o += 1

print(j)
print(o)

