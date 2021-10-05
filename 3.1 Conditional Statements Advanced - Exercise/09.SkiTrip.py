nights = int(input()) - 1
room_type = input()
feedback = input()

price = 0
room_one_person = 18
apartment = 25
president_apartment = 35

if room_type == "room for one person":
    price = room_one_person * nights
elif room_type == "apartment":
    if 0 < nights <= 10:
        price = apartment * 0.7 * nights
    elif 10 < nights <= 15:
        price = apartment * 0.65 * nights
    else:
        price = apartment * 0.5 * nights
elif room_type == "president apartment":
    price = president_apartment * nights

    if 0 < nights <= 10:
        price *= 0.9
    elif 10 < nights <= 15:
        price *= 0.85
    else:
        price *= 0.8

if feedback == "positive":
    price *= 1.25
else:
    price *= 0.9
print(f"{price:.2f}")

'''
30
president apartment
negative
'''
