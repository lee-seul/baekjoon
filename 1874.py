# coding: utf-8

import sys
write = sys.stdout.write
read = sys.stdin.readline

n = int(input())

stack = []
input_list = []
result = []

for _ in range(n):
    val = int(read())
    input_list.append(val)

u = True
index = 0
i = 1
while index < len(input_list):
    if i > input_list[index]:
        if stack[-1] == input_list[index]:
            stack.pop()
            result.append("-")
            index += 1
        else:
            u = False
            break
    else:
        stack.append(i)
        result.append("+")
        i += 1

#for _ in range(len(stack)):
#    result.append("-")

if u:
    for s in result:
        write(s+"\n")
else:
    print("NO")

