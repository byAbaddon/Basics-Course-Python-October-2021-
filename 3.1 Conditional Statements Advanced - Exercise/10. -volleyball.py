#volleyball
import math

type_year = input()
holiday_weekend = int(input())
simple_weekend = int(input())
weekend = (48 - simple_weekend) * 3 / 4 
holiday = (holiday_weekend * 2.0) / 3
allGames = weekend + holiday + simple_weekend

print(math.floor(allGames * 115 / 100) if type_year == 'leap' else  math.floor(allGames))



'''
leap
5
2
'''
#noramal, 6, 13
