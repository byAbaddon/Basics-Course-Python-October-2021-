# sumPrimeNonPrime
prime_num_sum, non_prime_num_sum = 0, 0
arr_prime_num = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61',
                 '67', '71', '73', '79', '83', '89', '97', '101', '103', '107', '109', '113', '127', '131', '137',
                 '139', '149', '151', '157', '163', '167', '173', '179', '181', '191', '193', '197', '199', '211',
                 '223', '227', '229', '233']
collection_list = []
el = input()

while el != 'stop':
    collection_list.append(int(el))
    el = input()

for index in range(0, len(collection_list)):
    if collection_list[index] < 0:
        print('Number is negative.')
        continue

    if str(collection_list[index]) in arr_prime_num:
        prime_num_sum += collection_list[index]
    else:
        non_prime_num_sum += collection_list[index]

print(f'Sum of all prime numbers is: {prime_num_sum}')
print(f'Sum of all non prime numbers is: {non_prime_num_sum}')

# 3, 9, 0, 7, 19, 4, stop
