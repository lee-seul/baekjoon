# coding: utf-8

def empty():
    if len(stack) == 0:
        return True
    return False

def top():
    if not empty():
        return stack[-1]
    return -1

def op_order(op):
    if op == "*" or op == "/":
        return 2
    elif op == "+" or op == "-":
        return 1
    else:
        return 0

def is_possible(ex):
    n = 0
    idx = 0
    while idx < len(ex):
        if ex[idx] == "(":
            n += 1
        elif ex[idx] == ")":
            n -= 1
        if n < 0:
            return False
        idx+=1
    if n == 0:
        return True
    return False

op_list = ["+", "-", "*", "/"]

ex = input()
possible = True

postfix = []
stack = []

if is_possible(ex):
    index = 0
    num = ""
    while index < len(ex):
        if ex[index] >= "0" and ex[index] <= "9":
            num += ex[index]
        else:
            if len(num) > 0:
                postfix.append(int(num))
                num = ""
            if ex[index] == "(":
                stack.append(ex[index])
            elif ex[index] == ")":
                while True:
                    top_val = top()
                    if top_val == "(":
                        stack.pop()
                        break
                    else:
                        postfix.append(stack.pop())
            elif ex[index] in op_list:
                while True:
                    top_val = top()
                    if op_order(ex[index]) <= op_order(top_val):
                        postfix.append(stack.pop())
                    else:
                        break
                stack.append(ex[index])
        index += 1
    if len(num) > 0:
        postfix.append(int(num))
    
    for _ in range(len(stack)):
        postfix.append(stack.pop())

else:
    possible = False

cnt = 0
for x in op_list:
    cnt += postfix.count(x)

if possible and len(postfix) - cnt == cnt + 1 and len(postfix) > 0:
    index = 0
    while index < len(postfix):
        if type(postfix[index]) == type(1):
            stack.append(postfix[index])
        else:
            result = 0
            val1 = stack.pop()
            val2 = stack.pop()
            if postfix[index] == "+":
                result = val2 + val1
            elif postfix[index] == "-":
                result = val2 - val1
            elif postfix[index] == "*":
                result = val2 * val1
            elif postfix[index] == "/":
                result = val2 // val1
            stack.append(result)
        index += 1
    print(stack.pop())
else:
    print("ROCK")



