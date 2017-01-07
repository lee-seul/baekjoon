# coding: utf-8

word = input().upper()
dic = {chr(i):0 for i in range(65,91)}
for key in dic.keys():
    dic[key] = word.count(key)

value = list(dic.values())
value.sort()
value.reverse()
if value[0] == value[1]:
    print("?")
else:
    for key in dic.keys():
        if dic[key] == value[0]:
            print(key)
            break
