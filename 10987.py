# coding: utf-8

n = input()

result = 0
m = ["a", "e", "i", "o", "u"]

for i in m:
    result += n.count(i)

print(result)

