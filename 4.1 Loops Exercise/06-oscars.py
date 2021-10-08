actor, start_points, jury_count = [input() for x in range(3)]
all_points = [float(start_points)]
[all_points.append(len(input()) * float(input()) / 2) for x in range(int(jury_count)) if sum(all_points) < 1250.5]

if sum(all_points) >= 1250.5:
    print(f'Congratulations, {actor} got a nominee for leading role with {sum(all_points):.1f}!')
else:
    print(f'Sorry, {actor} you need {1250.5 - sum(all_points):.1f} more!')


'''
Zahari Baharov
205
4
Johnny Depp
45
Will Smith
29
Jet Lee
10
Matthew Mcconaughey
39
--------------------
Sandra Bullock
340
5
Robert De Niro
50
Julia Roberts
40.5
Daniel Day-Lewis
39.4
Nicolas Cage
29.9
Stoyanka Mutafova
33
'''
