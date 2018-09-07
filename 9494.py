# coding: utf-8


while True:
    n = int(input())
    if not n:
        break 
    idx = 0
    for i in range(n):
        string = input()
        for i, char in enumerate(string):
            if char == ' ' and idx <= i:
                idx = i
                break
    print(idx+1)
            
