# coding: utf-8


dic = {"000": "0", "001": "1", "010": "2", "011": "3", "100": "4",
       "101": "5", "110": "6", "111": "7"}

number = input()

while len(number) % 3:
    number = "0" + number


result = ""
for i in range(0, len(number), 3):
    key = number[i:i+3]
    result += dic[key]

print(result)

