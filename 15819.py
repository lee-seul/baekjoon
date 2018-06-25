# coding: utf-8


n, i = map(int, input().split())

words = []
for _ in range(n):
    s = input()
    words.append(s)

words.sort()
print(words[i-1])
