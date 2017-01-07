# coding: utf-8

def check_han(num):
    num = str(num)
    if len(num) <= 2:
        return True
    else:
        for i in range(len(num)-2):
            if int(num[i+1]) - int(num[i]) != int(num[i+2]) - int(num[i+1]):
                return False
        return True

a = int(input())

result = 0
for i in range(1, a+1):
    if check_han(i):
        result += 1
print(result)

