# coding: utf-8 


def solution(bark, rest, time):
    moduler = bark + rest
    result = time % moduler
    if result <= bark and result != 0:
        return 1
    return 0


a, b, c, d = map(int, input().split())
people = map(int, input().split())


for person in people:
    result = 0
    result += solution(a, b, person)
    result += solution(c, d, person)
    print(result)


