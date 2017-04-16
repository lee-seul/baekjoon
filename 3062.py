# coding: utf-8


def check_palindrom(num):
    reverse_num = list(num)
    reverse_num.reverse()
    reverse_num = "".join(reverse_num)

    num = int(reverse_num) + int(num)
    num = str(num)
    length = len(num) - 1
    
    for i in range((length+1)//2):
        if num[i] != num[length-i]:
            return False
    return True


t = int(input())

for _ in range(t):
    n = input()
    if check_palindrom(n):
        print("YES")
    else:
        print("NO")

