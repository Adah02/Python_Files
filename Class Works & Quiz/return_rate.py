investment_amount = int(input('Enter investment amount: '))
percentage_interest_rate = int(input('Enter interest rate in percentage: '))
number_of_years = int(input('Enter number of years for investment: '))

PERCENTAGE = 100
actual_rate = (percentage_interest_rate / PERCENTAGE)

print('Years \t Return amount')
counter = 1
interest_amount = 0

while counter != number_of_years:
  interest_amount += investment_amount * (1 + actual_rate)
  print(f'{counter} \t {interest_amount:,.2f}')
  counter += 1