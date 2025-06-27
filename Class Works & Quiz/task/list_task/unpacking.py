def list_practice(my_list):
    num1, num2, num3, *others = my_list
    return num1, num2, num3

def is_odd(my_list):
    return my_list % 2 != 0

def filtered_list(my_list):
    return list(filter(is_odd, my_list))

def filtered_with_lambda(my_list):
    return list(filter(lambda number: number % 2 != 0, my_list))

def sum_of_numbers(my_list):
    sum_of_list = sum(map(lambda number: number, my_list))
    return sum_of_list

my_list = [8, 4, 1, 6, 7, 3, 12, 13]

print('with normal filter function', filtered_list(my_list))
print('with lambda filter function', filtered_with_lambda(my_list))
print('Sum of list using map',sum_of_numbers(my_list))