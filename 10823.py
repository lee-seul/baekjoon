# coding: utf-8


import sys


s = sys.stdin.readlines()
s = ''.join(s)
s = s.replace('\n', '')

print(sum(map(int, s.split(','))))

