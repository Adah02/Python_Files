import random

def length_of_list(numbers):
    numbers_length = 0
    for index in numbers:
        numbers_length += 1

    return numbers_length

def sum_of_elements_in_even_positions(numbers):
    sum = 0
    counter = 0
    for item in numbers:
        if counter % 2 == 0:
            sum += item
        counter += 1
    return sum


def sum_of_elements_in_odd_positions(numbers):
    sum_of_odd = 0
    counter = 0
    for item in numbers:
        if counter % 2 != 0:
            sum_of_odd += item
        counter += 1
    return sum_of_odd


def multiple_of_numbers_in_third_positions(numbers):
    multiple = 1
    counter = 1
    for item in numbers:
        if counter % 3 == 0:
            multiple *= item
        counter += 1

    return multiple

def average_of_list(numbers):
    total = 0
    length_of_numbers = 0
    for number in numbers:
        total += number
        length_of_numbers += 1
    average = total / length_of_numbers

    return average


numbers = []

for i in range(50):
    random_numbers = random.randrange(1, 50)
    numbers.append(random_numbers)

