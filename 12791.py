# coding: utf-8

albums = [(1967, "DavidBowie"), (1969, "SpaceOddity"), 
(1970, "TheManWhoSoldTheWorld"), (1971, "HunkyDory"),
(1972, "TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars"),
(1973, "AladdinSane"), (1973, "PinUps"), (1974, "DiamondDogs"),
(1975, "YoungAmericans"), (1976, "StationToStation"), (1977, "Low"),
(1977, "Heroes"), (1979, "Lodger"), (1980, "ScaryMonstersAndSuperCreeps"),
(1983, "LetsDance"), (1984, "Tonight"), (1987, "NeverLetMeDown"),
(1993, "BlackTieWhiteNoise"), (1995, "1.Outside"), (1997, "Earthling"),
(1999, "Hours"), (2002, "Heathen"), (2003, "Reality"), 
(2013, "TheNextDay"), (2016, "BlackStar")]

t = int(input())

result = []
for _ in range(t):
    year, to_year = map(int, input().split())  
    temp = []
    for album in albums:
        if year <= album[0] <= to_year:
            temp.append(album)

    result.append(len(temp))
    result += temp

for r in result:
    if type(r) is type(1):
        print(r)
    else:
        print(str(r[0]), r[1])

