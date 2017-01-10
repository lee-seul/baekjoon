# coding: utf-8

import sys

n = int(input())
words = []
for _ in range(n):
    words.append(sys.stdin.readline())

words = list(set(words))
words.sort()
length = 1
dictionary = []
while len(words) != len(dictionary):
    for i, word in enumerate(words):
        if len(word) == length:
            dictionary.append(word)
    length += 1

for word in dictionary:
    sys.stdout.write(word) 
    
