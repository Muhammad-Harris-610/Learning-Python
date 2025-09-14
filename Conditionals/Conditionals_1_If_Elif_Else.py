# Conditionals: Exercise 1 (Basic if-elif-else statements)

# Program 1: Alien Game
alien_color = 'red'
if alien_color == 'green':
   print('You just earned 5 points!')
elif alien_color == 'yellow':
   print('You just earned 10 points!')
elif alien_color == 'red':
   print('You just earned 15 points!')

# Program 2: Stage of life
age = 18
if age < 2:
   print('You are a baby.')
elif age < 4:
   print('You are a toddler.')
elif age < 13:
   print('You are a kid.')
elif age < 20:
   print('You are a teenager.')
elif age < 65:
   print('You are an adult.')
elif age >= 65:
   print('You are an elder.')

# Program 3: Favorite Fruits
fruits = ['Dates', 'Plums', 'Apples']
if 'Dates' in fruits:
   print('You really like Dates!')
if 'Mangoes' in fruits:
   print('You really like Mangoes!')
if 'Plums' in fruits:
   print('You really like Plums!')
if 'Oranges' in fruits:
   print('You really like Oranges!')
if 'Apples' in fruits:
   print('You really like Apples!')