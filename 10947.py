# coding: utf-8

import random
lotto = [i for i in range(1, 46)]

for _ in range(6):
    random.shuffle(lotto)
    print(lotto.pop(), end=" ")

