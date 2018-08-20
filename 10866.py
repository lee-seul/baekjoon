# coding: utf-8


import sys


def sys_print(value=-1):
    return sys.stdout.write(str(value)+'\n')


class Deq:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __getitem__(self, position):
        return self._data[position]

    def _insert(self, value, position):
        self._data.insert(position, value)

    def _pop(self, position):
        return self._data.pop(position)

    def _is_empty(self):
        if not len(self):
            return True
        return False

    def push(self, value, position=-1):
        if not position == -1:
            self._insert(position, value)
            return 
        self._data.append(value)

    def pop_data(self, position=-1):
        if self._is_empty():
            return sys_print()
        return sys_print(self._pop(position))

    def empty(self):
        if self._is_empty():
            return sys_print(1)
        return sys_print(0)

    def front(self):
        if self._is_empty():
            return sys_print()
        return sys_print(self[0])

    def back(self):
        if self._is_empty():
            return sys_print()
        return sys_print(self[-1])
    
    def size(self):
        return sys_print(len(self))


n = int(input())

d = Deq()
for _ in range(n):
    statement = sys.stdin.readline().strip()
    statement = statement.split()
    s = statement[0]
    if s == 'push_back':
        d.push(statement[1])

    if s == 'push_front':
        d.push(statement[1], 0)

    if s == 'pop_front':
        d.pop_data(0)

    if s == 'pop_back':
        d.pop_data()

    if s == 'size':
        d.size()

    if s == 'empty':
        d.empty()

    if s == 'front':
        d.front()

    if s == 'back':
        d.back()

