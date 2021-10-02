chicken, fish, vegetable = [int(input()) for _ in range(3)]
total_menu_price = chicken * 10.35 + fish * 12.40 + vegetable * 8.15
dessert = total_menu_price * 0.20
delivery = 2.5

print(total_menu_price + dessert + delivery)

'''
2
4
3

output: 116.2
'''
