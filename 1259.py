# coding: utf-8

def is_palindrome(num):
    num = str(num)
    for i in range((len(num)+1)//2):
        if num[i] != num[-(i+1)]:
            return False
    return True

while True:
    n = int(input())
    if not n:
        break
    if is_palindrome(n):
        print("yes")
    else:
        print("no")
