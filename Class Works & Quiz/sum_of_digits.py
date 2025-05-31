def sum_digits(user_input):
  sum_of_digits = 0
  number_value = user_input
  while number_value != 0:
    remainder = number_value % 10
    sum_of_digits += remainder
    number_value = number_value // 10
  return sum_of_digits

user_input = int(input("Enter the integer of choice: "))
outcome = sum_digits(user_input)
print('Sum of digits is ',outcome)