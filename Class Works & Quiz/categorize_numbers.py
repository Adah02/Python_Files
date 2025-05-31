def categorize_numbers(values, divisor):
  divisible = 0
  non_divisible = 0
  if values // divisor == 0:
    print(values, end =" ")
    divisible += 1
  if values // divisor != 0:
    non_divisible += 1

  if divisible >= 1:
    return values
  else: print('No divisible number found')
  return non_divisible
    

divisor = float(input('Enter divisor: '))
values = input('Enter number: ')

while values != 0:
  values = float(input('Enter number: '))
result = categorize_numbers(values,divisor)
print(result)