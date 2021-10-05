search = input()
collections = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes", "tomato", "cucumber", "pepper", "carrot"]

if search in collections:
    print("fruit" if collections.index(search) <= 5 else "vegetable")
else:
    print("unknown")

# banana

