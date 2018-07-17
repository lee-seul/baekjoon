# coding: utf-8


ignores = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

words = input().split()

result = ''
for idx, word in enumerate(words):
    if word not in ignores or not idx:
        result += word[0].upper()

print(result)
