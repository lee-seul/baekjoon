# coding: utf-8

h = input()
dic = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F': 15}
h = list(h)
h.reverse()
result = 0
for i in range(len(h)):
    if h[i] in dic.keys():
        result += dic[h[i]] * (16**i)
    else:
        result += int(h[i]) * (16**i)

print(result)

