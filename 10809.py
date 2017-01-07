# coding: utf-8

word = input()
dic = {chr(i):-1 for i in range(97, 123)}
for i in range(len(word)):
    if dic[word[i]] == -1:
        dic[word[i]] = i

for key in sorted(dic.keys()):
    print(dic[key], end=" ")


