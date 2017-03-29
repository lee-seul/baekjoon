# coding: utf-8


op_order = {"-": 1, "+": 1, "*": 2, "/": 2, "(": 0}

ex = input()
stack = []

for c in ex:
    if c in op_order.keys():
        if not stack or c == '(':
            stack.append(c)
        else:
            while stack and op_order[c] <= op_order[stack[-1]]:
                print(stack.pop(), end='')
            stack.append(c)
    
    elif c == ')':
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')

        if stack and stack[-1] == '(':
            stack.pop()

    else:
        print(c, end='')     

while stack:
    print(stack.pop(), end='')
 
