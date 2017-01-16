# coding: utf-8

def is_awesome(num):
    result = "" 
    for i in range(30, -1, -1):    
        if num >= 2 ** i:
            num -= 2 ** i
            result += "1"
        elif num < 2 ** i and "1" in result:
            result += "0"
    if "111" in result or "000" in result:
        return True
    return False
    

l, r = map(int, input().split())

result = 0
for i in range(7, r+1):
    if is_awesome(i):
        result += 1

print(result)
