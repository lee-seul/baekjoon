# coding: utf-8


def get_max_value(dic, max_value):
    keys = []
    for key in dic.keys():
        if dic[key] == max_value:
            keys.append(key)
    keys.sort()
    return keys[0]


n = int(input())

dic = {}
for _ in range(n):
    book = input()
    if not book in dic:
        dic[book] = 0
    dic[book] += 1

max_value = max(dic.values())
print(get_max_value(dic, max_value))
