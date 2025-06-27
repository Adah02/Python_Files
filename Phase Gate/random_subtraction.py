import random

correctAnswer = 0
attempt = 0

for index in range(10):
	first_number = random.randrange(20)
	second_number = random.randrange(20)
	for count in range(2):
		temp = first_number
		if first_number < second_number:
			first_number = second_number
			second_number = temp
		if first_number > second_number & count != 2:
			print(f'What is {first_number} - {second_number}')
			answer = int(input('Enter answer: '))
			if answer == (first_number - second_number):
				correctAnswer += 1
				attempt += 1
				break
			else: attempt += 1


print(f'The number of correct answers is {correctAnswer} and attempts is {attempt}')
print(f'Your score is {(correctAnswer / attempt) * 100 :.1f} %')
