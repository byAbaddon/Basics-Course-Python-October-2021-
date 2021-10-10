bad_grades = int(input())
count_bad_grades = bad_grades
name_task = input()
collection_dict = {}

while name_task != 'Enough':
    grades = int(input())
    if grades <= 4:
        bad_grades -= 1
    if bad_grades == 0:
        print(f'You need a break, {count_bad_grades} poor grades.')
        exit()

    collection_dict[name_task] = grades
    name_task = input()

average = sum(collection_dict.values()) / len(collection_dict.values())
print(f'Average score: {average:.2f}')
print(f'Number of problems: {len(collection_dict)}')
print(f'Last problem: {list(collection_dict.keys())[-1]}')

# 2 , Income , 3, Game Info, 6, Best Players, 4
