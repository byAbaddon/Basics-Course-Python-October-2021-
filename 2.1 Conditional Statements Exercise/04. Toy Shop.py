trip, puzzles, dolls, bears, minions, trucks = [float(input()) for _ in range(6)]

total_sum = puzzles * 2.6 + dolls * 3 + bears * 4.1 + minions * 8.2 + trucks * 2.0
toys_count = puzzles + dolls + bears + minions + trucks

if toys_count >= 50:
    total_sum *= 0.75

total_sum = total_sum * 0.9

print(f'Yes! {total_sum  - trip:.2f} lv left.' if total_sum >= trip
      else f'Not enough money! {trip - total_sum:.2f} lv needed.')


'''
40.8
20
25
30
50
10

output: Yes! 418.20 lv left.

---------------------------
320
8
2
5
5
1

output: Not enough money! 238.73 lv needed.
'''
