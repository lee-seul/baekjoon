# coding: utf-8 


n = int(input())
string = input().split('*')
front = len(string[0])
end = -len(string[1])

for _ in range(n):
    s = input()
    if string[0] == s[:front]: 
        s = s[front:]
        if string[1] == s[end:]:
            print('DA')
        else:
            print('NE')
    else:
        print('NE')
