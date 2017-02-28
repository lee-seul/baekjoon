# coding: utf-8

s = input()

result = 10
before = s[0]
for i in range(1, len(s)):
    if before == s[i]:
        result += 5
    else:
        result += 10
        before = s[i]

print(result)

