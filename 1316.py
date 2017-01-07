# coding: utf-8


def is_group(word):
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                return False
    return True


n = int(input())
cnt = 0
for _ in range(n):
    if is_group(input()):
        cnt += 1

print(cnt)
