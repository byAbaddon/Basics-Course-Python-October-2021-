degrees = int(input())
day_time = input()
result = 0
data_dict = {
    'm': {'Morning': 'Sweatshirt and Sneakers', 'Afternoon': 'Shirt and Moccasins', 'Evening': 'Shirt and Moccasins'},
    'a': {'Morning': 'Shirt and Moccasins', 'Afternoon': 'T-Shirt and Sandals', 'Evening': 'Shirt and Moccasins'},
    'e': {'Morning': 'T-Shirt and Sandals', 'Afternoon': 'Swim Suit and Barefoot', 'Evening': 'Shirt and Moccasins'},
}

if 10 <= degrees <= 18:
    result = data_dict['m'][day_time]
elif 18 < degrees <= 24:
    result = data_dict['a'][day_time]
elif degrees >= 25:
    result = data_dict['e'][day_time]

print(f"It's {degrees} degrees, get your {result}.")

'''
16
Morning
---------------
16
Afternoon
---------------
22
Afternoon
---------------
28
Evening
'''
