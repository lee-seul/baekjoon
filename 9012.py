# coding: utf-8


t = int(input())

for _ in range(t):
    s = input()
    stack = []
    result = "YES"
    for e in s:
        if e == "(":
            stack.append(e)
        elif e == ")": 
            if len(stack):
                stack.pop()
            else:
                result = "NO"
                break 
    if len(stack):
        result = "NO"
    print(result)
