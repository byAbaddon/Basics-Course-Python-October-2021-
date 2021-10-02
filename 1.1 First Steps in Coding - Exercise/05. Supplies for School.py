pens, markers, detergent, discount = [float(input()) for _ in range(4)]
price = pens * 5.8 + markers * 7.2 + detergent * 1.2
print(price * (100 - discount) / 100)

'''
2
3
4
25

output: 28.5
'''
