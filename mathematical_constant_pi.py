users_range = int(input('Enter your range: '))
actual_range = (users_range // 2)
e_constant = 4
pi_value = 4
terms = 0
negative_value = 3
positive_value = 5

for i in range(actual_range):
  pi_value -= (4 / negative_value)
  terms += 1
  print(f'{terms} \t {pi_value:.5f}')
  negative_value += 4
  for j in range(1):
    pi_value += (4 / positive_value)
    terms += 1
    positive_value += 4
    print(f'{terms} \t {pi_value:.5f}')
  if pi_value == 3.14:
    print(f'The value for pi is {pi_value:.5f} at term {terms}')
    continue
  elif pi_value == 3.141:
    print(f'The value for pi is {pi_value:.5f} at term {terms}')
    continue
  elif pi_value == 3.1415:
    print(f'The value for pi is {pi_value:.5f} at term {terms}')
    continue

   
