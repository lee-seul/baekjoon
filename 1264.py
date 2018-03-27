# coding: utf-8


import sys

l = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

results = []

while True:
    result = 0
    string = sys.stdin.readline().rstrip()
    if string == '#':
        break
    for char in string:
        if char in l:
            result += 1
    results.append(result) 

for result in results:
    sys.stdout.write(str(result) + '\n')


