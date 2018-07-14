# coding: utf-8


def run_eval(value1, value2, oper, result):
    temp = '{}{}{}'.format(value1, oper, value2)
    if eval(temp) == result:
        return True
    return False


def opers_iter(value1, value2, value3):
    opers = ['*', '/', '+', '-']
    for oper in opers:
        result = run_eval(value1, value2, oper, value3)
        if result:
            print('{}{}{}={}'.format(value1, oper, value2,value3))
            return

    for oper in opers:
        result = run_eval(value2, value3, oper, value1)
        if result:
            print('{}={}{}{}'.format(value1, value2, oper, value3))
            return 


a, b, c = map(int, input().split())

opers_iter(a, b, c)

