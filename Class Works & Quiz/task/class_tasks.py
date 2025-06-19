import random

def length_of_list(numbers):
    numbers_length = 0
    for item in numbers:
        numbers_length += 1

    return numbers_length

def sum_of_elements_in_even_positions(numbers):
    sum = 0
    length = 0
    for index in numbers:
        length += 1

    for item in range(0, length, 2):
        sum += numbers[item]
    return sum


def sum_of_elements_in_odd_positions(numbers):
    sum_of_odd_index = 0
    length = 0
    for index in numbers:
        length += 1

    for item in range(1, length, 2):
        sum_of_odd_index += numbers[item]
    return sum_of_odd_index


def multiple_of_number_in_third_positions(numbers):
    multiple = 1
    length = 0
    for index in numbers:
        length += 1

    for item in range(0, length, 3):
        multiple *= numbers[item]
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


print("Number of items in list ",length_of_list(numbers))
print('Sum of elements in even positions', sum_of_elements_in_even_positions(numbers))
print("Multiple of numbers at third index: ", multiple_of_number_in_third_positions(numbers))

print("Average of list ",average_of_list(numbers))

