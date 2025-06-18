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