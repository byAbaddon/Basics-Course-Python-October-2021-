from math import ceil

movie, duration, breack = input(), int(input()), int(input())

lunch = breack / 8
relax = breack / 4
total_time = breack - lunch - relax

if total_time >= duration:
    print(f'You have enough time to watch {movie} and left with {ceil(total_time - duration)} minutes free time.')
else:
    print(f"You don't have enough time to watch {movie}, you need {ceil(duration - total_time)} more minutes.")
    
'''
Game of Thrones
60
96
'''
