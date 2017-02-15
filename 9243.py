# coding: utf-8

def delete(str1):
    length = len(str1)
    result = ""
    for i in range(length):
        if str1[i] == "0":
            result += "1"
        elif str1[i] == "1":
            result += "0"
    return result

n = int(input())

a = input()
b = input()

if n % 2:
    a = delete(a)

if a == b:
    print("Deletion succeeded")
else:
    print("Deletion failed")
