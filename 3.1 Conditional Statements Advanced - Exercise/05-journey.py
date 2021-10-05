# journey
budget = float(input())
season = input()
country = place = ''

if budget <= 100:
    country = 'Bulgaria'
    if season == 'summer':
        place = 'Camp'
        budget *= 0.30
    else:
        place = 'Hotel'
        budget *= 0.70

elif 100 < budget <= 1000:
    country = 'Balkans'
    if season == 'summer':
        place = 'Camp'
        budget *= 0.40
    else:
        place = 'Hotel'
        budget *= 0.80
elif budget > 1000:
    country = 'Europe'
    place = 'Hotel'
    budget *= 0.90

print(f'Somewhere in {country}\n{place} - {budget:.2f}')

# 50, summer
# 1500, summer
