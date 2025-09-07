# Lists: Exercise 1 (Working with indices)

names = ['Taha', 'Abdul Hadi', 'Osaid', 'Abdullah', 'Ibrahim']

# Using the list in messages (greetings)
print(f'Assalam-u-Aleykum {(names[0])}')
print(f'Sub-a-Khair {(names[1])}')
print(f'Gunaydin {(names[2])}')
print(f'Hos Geldin {(names[3])}')
print(f'Selmaun Aleykum {(names[4])}')

names.append('Harris')
print(f'Merhaba {names[-1]}')

names.insert(3, 'Ilyas')
print(f'Hayirli Sabahlar {names[3]}')
print(names)

not_friend = names.pop()
print(f'{not_friend} is not my friend anymore.')
print(names)

imaginary_friend = 'Ilyas'
names.remove(imaginary_friend)
print(f'{imaginary_friend} was my iota friend.')
print(names)