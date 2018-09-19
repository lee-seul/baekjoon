# coding: utf-8


class Container:

    def __init__(self, max_length):
        self._max_length = max_length
        self._container = []
        self._data = {}
        self.c = 0

    def __len__(self):
        return len(self._container)

    def __iter__(self):
        return iter(self._container)
    
    def _change(self, num):
        temp = []
        for key in self._data.keys():
            if self._data[key] == 1:
                temp.append(key)
        
        for i, n in enumerate(self._container):
            if n in temp:
                self._container[i] = num
                break
    
    def vote(self, num):
        if num in self._data:
            self._data[num] += 1
            return

        self._data[num] = 1
        if len(self) < self._max_length:
            self._container.append(num)
            return
        self._change(num)


n = int(input())
t = int(input())
numbers = [int(x) for x in input().split()]

c = Container(n)
for number in numbers:
    c.vote(number)

for value in c:
    print(value, end=' ')
