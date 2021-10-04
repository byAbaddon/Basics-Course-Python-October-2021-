n = float(input())
bonus = 0

if n <= 100:
    bonus = n + 5
elif 100 < n <= 1000:
    bonus = n * 1.20
elif n > 1000:
    bonus = n * 1.10

if n % 2 == 0:
    bonus += 1

if n % 10 == 5:
    bonus += 2

points = bonus - n
print(f'{points}\n{bonus}')

# 20
