# coding: utf-8


num1, num2 = map(list, input().split())

stack = []

length = min([len(num1), len(num2)])
for _ in range(length):
    temp = int(num1.pop()) + int(num2.pop())
    stack.append(str(temp))

while num1:
    stack.append(str(num1.pop()))

while num2:
    stack.append(str(num2.pop()))

result = ""
for _ in range(len(stack)):
    result += stack.pop() 

print(result)

