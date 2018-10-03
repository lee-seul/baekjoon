# coding: utf-8


import sys


dic = {chr(x):0 for x in range(97, 123)}

s = sys.stdin.readlines()
s = ''.join(s)
s = s.replace('\n', '')

for char in s:
    if char in dic:
        dic[char] += 1

temp = []
for key in dic.keys():
    temp.append((key, dic[key]))

temp = sorted(temp, key=lambda x: x[1], reverse=True)

ans = temp[0][1]
result = [x[0] for x in temp if x[1] == ans]
result.sort()
print(''.join(result))

