# coding: utf-8

def is_ascend(li):
    for i in range(8):
        if li[i] != i+1:
            return False
    return True

def is_descend(li):
    a = 8
    for i in range(8):
        if li[i] != a:
            return False
        a -= 1
    return True

l = list(map(int, input().split()))

if is_ascend(l):
    print("ascending")
elif is_descend(l):
    print("descending")
else:
    print("mixed")
