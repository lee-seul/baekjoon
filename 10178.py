# coding: utf-8

t = int(input())

for _ in range(t):
    total, boys = map(int, input().split())
    print("You get {} piece(s) and your dad gets {} piece(s).".format(\
            total//boys, total%boys))
    
    #print(f"You get {total//boys} piece(s) and your dad gets \
    #        {total%boys} piece(s).")
