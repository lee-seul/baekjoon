# coding: utf-8

def empty():
    if len(stack) == 0:
        return True
    return False

def top():
    if not empty():
        return stack[-1]
    return -1

op_list = ["-", "+", "*", "/"]

def op_order(op):
    if op == "*" or op == "/":
        return 2
    elif op == "+" or op == "-":
        return 1
    else: # op == "("
        return 0

ex = input()
postfix = ""

stack = []

index = 0
while index < len(ex):
    if ex[index] not in op_list and ex[index] != "(" and ex[index] != ")":
        postfix += ex[index]
    elif ex[index] == "(":
        stack.append(ex[index])
    elif ex[index] in op_list:
        while True:
            top_val = top()
            if op_order(ex[index]) <= op_order(top_val):
                postfix += stack.pop()
            else:
                break 
        stack.append(ex[index])
    elif ex[index] == ")":
        while True:
            top_val = top()
            if top_val == "(":
                stack.pop()
                break
            else:
                postfix += stack.pop()
    index += 1

for _ in range(len(stack)):
    postfix += stack.pop()

print(postfix)




