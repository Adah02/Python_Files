amount_invested = int(input('Enter the amount invested: '))
percentage_rate = int(input('Enter percentage rate: '))
number_of_years = int(input('Enter number of year(s): '))

actual_rate = percentage_rate / 100
return_amount = amount_invested * ((1 + actual_rate)**(number_of_years))

print('Your return amount at the end of year', number_of_years,'is ', return_amount)

