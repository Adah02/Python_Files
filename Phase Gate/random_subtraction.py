import random

correctAnswer = 0
attempt = 0

for index in range(11):
	first_number = random.randrange(20)
	second_number = random.randrange(20)
	for count in range(3):
		if first_number > second_number & count != 2:
			print(f'What is {first_number} - {second_number}')
			answer = int(input('Enter answer: '))
			if answer == (first_number - second_number):
				correctAnswer += 1
				attempt += 1
				break;
			else: attempt += 1


print(f'The number of correct anwers is {correctAnswer} and attempts is {attempt}')
