amount_invested = int(input('Enter the amount invested: '))
percentage_rate = int(input('Enter percentage rate: '))

print('Your return amount after 30 years')
actual_rate = percentage_rate / 100

for year in range(1, 30 + 1):
  return_amount = amount_invested * ((1 + actual_rate)**(year))
  print(f'{year} \t $ {return_amount:>.2f}')

