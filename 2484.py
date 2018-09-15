# coding: utf-8


from collections import Counter


class Container:

    def __init__(self, dic):
        self._list = [(key, dic[key]) for key in dic.keys()]
        self._list = sorted(self._list, key=lambda x: x[1], reverse=True)
        self._length = len(self._list)

    def money(self):
        length = self._length
        items = self._list

        if length == 1:
            value = items[0][0]
            return 50000 + (value * 5000)

        if length == 2:
            if items[0][1] == 3:
                value = items[0][0]
                return 10000 + (value * 1000)
            else:
                return 2000 + (items[0][0] * 500) + (items[1][0] * 500)
        
        if length == 3:
            return 1000 + (items[0][0] * 100)

        items.sort(reverse=True)
        return 100 * items[0][0]



n = int(input())

ma = 0
for _ in range(n):
    numbers = [int(x) for x in input().split()]
    numbers = Counter(numbers)
    c = Container(numbers)
    m = c.money()
    if ma < m:
        ma = m

print(ma)
    

