# coding: utf-8


import datetime

# 서버 시간은 UTC이므로
now = datetime.datetime.now() + datetime.timedelta(hours=9)
print(now.year)
print(now.month)
print(now.day)
