# coding: utf-8

dice = list(map(int, input().split()))

dice_set = set(dice)
length = len(dice_set)

dice.sort()
result = 0
if length == 1:
    result = 10000 + 1000 * dice[0]
elif length == 2:
    result = 1000 + 100 * dice[1]
else:
    result = 100 * dice[2]

print(result)

