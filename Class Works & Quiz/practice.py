numbers = []
for i in range(6):
	numbers.append(i)

print(numbers)

number_2 = list(range(6))

multiple = [item**3 for item in range(6)]
print(multiple)

#To reverse a list
numbers.reverse()

numbers.pop()
print(numbers)

#To clear a list
numbers.clear()
numbers[:] = []

print(number_2)
print(numbers)

colors = ['red', 'orange', 'yellow', 'green', 'blue']

print(colors)

colors1 = [item.upper() for item in colors]

print(colors1)

#Printing the cubes of integers alongside
cubes = [(number, number**3) for number in range(1, 11)]

print(cubes)

#Printing the square of even numbers in a series

number = [4, 1, 6, 8, 7, 3, 2, 1, 9, 11, 10]

for value in (x**2 for x in number if x % 2 == 0):
	print(value, end = ' ')

