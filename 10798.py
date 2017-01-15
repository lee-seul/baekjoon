# coding: utf-8

string = []

for _ in range(5):
    string.append(input())

blank = " "
for i in range(5):
    string[i] += blank * (15 - len(string[i]))

result = ""

for i in range(15):
    for j in range(5):
        result += string[j][i]

result = result.replace(" ", "")
print(result)
    
