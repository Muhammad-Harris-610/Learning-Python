# Lists and Loops: Exercise 2 (Working with range, list, min, max and sum functions along with list comprehension)

# Program 1
numbers = list(range(1, 1001))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Program 2
odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

# Program 3
threes = list(range(3, 31, 3))
print(threes)

# Program 4
cubes = [value**3 for value in range(1, 10)]
print(cubes)
