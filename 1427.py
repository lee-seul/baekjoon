# coding: utf-8


n = input()

counting = [0 for _ in range(10)]
for num in n:
    counting[int(num)] += 1

result = ""
for i in range(9, -1, -1):
    result += str(i) * counting[i]

print(result)
