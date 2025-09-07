# Lists and Loops: Exercise 3 (sliced Lists)

# Slicing Lists
locations = ['Mecca', 'Medina', 'Jerusalem', 'Damascus', 'Hebron', 'Kufa', 'Basra', 'Antioch']
print(f'The first three items in the list are {locations[:3]}')
print(f'Four items from the middle of the list are {locations[2:-2]}')
print(f'The last three items in the list are {locations[-3:]}')

# Slicing and Copying Lists
my_foods = ['Biryani', 'Karahi', 'Paaye']
friend_foods = my_foods[:]
my_foods.append('Nehaari')
friend_foods.append('Pulao')
print(f'My favorite foods are {my_foods}')
print(f"My friend's favorite foods are {friend_foods}")