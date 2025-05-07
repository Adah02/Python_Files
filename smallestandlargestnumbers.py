score = int(input('Enter integer: '))
largest = score
smallest = score

for number in range(9):
	if (score > largest): largest = score
	if (score < smallest): smallest = score
	score = int(input('Enter integer: '))

print(f"The smallest is {smallest} and the largest is {largest}")