def accessing_third_element(nums):
    return nums[2]

def changing_last_element(colors, users_choice):
    colors[-1] = users_choice
    return colors

def adding_item_to_list(colors, choice):
    colors.append(choice)
    return colors

def removing_third_element(first_list):
    first_list.remove(3)
    return first_list

def length_of_elements(names):
    length = []
    for item in names:
        length.append(len(item))

    return length

def ascending_list(numbers):
    numbers.sort()
    return numbers

def list_of_even_numbers(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)

    return even

def combining_list(a, b):
    a.extend(b)
    return a

def elements_greater_than_three_in_list(living_things):
    new_list = []
    for item in living_things:
        if len(item) > 3:
            new_list.append(item)

    return new_list


nums = [10, 20, 30, 40, 50]
colors = ['red', 'green', 'blue']
first_list = [1, 2, 3, 4, 5]
names = ['Alice', 'Bob', 'Charlie']
numbers = [4, 1, 3, 9, 2]
a = [1, 2, 3]
b = [4, 5, 6]
living_things = ['lamb', 'kit', 'yam', 'kings', 'dogs', 'man']