# Conditionals: Exercise 2 (Using Conditions with Lists and Loops)

# Program 1: Assigning Greetings
usernames = []
if usernames:
   for username in usernames:
      if username == 'Admin':
         print(f'Assalam-u-Aleykum wa Rahmatullah {username}')
      else:
         print(f'Assalam-u-Aleykum {username}')
else:
   print('We need to find some users!')


# Program 2: Assigning Usernames
current_users = ['Taha', 'Abdul Hadi', 'Osaid', 'Abdullah', 'Ibrahim']
lower_current_users = [name.lower() for name in current_users]
new_users = ['Nooh', 'Ibrahim', 'Taha', 'Moosa', 'Esa']

for user in new_users:
   if user.lower() in lower_current_users:
      print('Username already taken; enter a new username.')
   else:
      print('Username is available.')

# Program 3: Ordinal Numbers
numbers = list(range(1, 10))
for number in numbers:
   if number == 1:
      ordinal = 'st'
   elif number == 2:
      ordinal = 'nd'
   elif number == 3:
      ordinal = 'rd'
   else:
      ordinal = 'th'
   print(f'{number}{ordinal}')

