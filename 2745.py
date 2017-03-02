# coding: utf-8

dic = {str(x):x for x in range(10)}
dic.update({chr(x):x-55 for x in range(65, 91)})

num, digit = input().split()
digit = int(digit)

num = list(num)
num.reverse()

result = 0
for i in range(len(num)):
    result += dic[num[i]] * (digit ** i)

print(result)

