print('Enter an integer of five-digits: ')
number = int(input())

first_digit = number // 10000
second_digit = number // 1000 % 10
third_digit = number // 100 % 10
fourth_digit = number // 10 % 10
fifth_digit = number % 10 

print(first_digit,' ',second_digit,' ',third_digit,' ',fourth_digit,' ',fifth_digit)
