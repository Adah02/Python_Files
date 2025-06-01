cent_amount = int(input('Enter change in cent: '))

final_quarters = 25
final_dimes = 10
final_nickels = 5
final_penny = 1

print('Your change is:')
quarters = cent_amount // 25
print(f'{quarters} quarters')

quarters_remainder = cent_amount % 25
if quarters_remainder >= final_dimes:
  dimes = quarters_remainder // final_dimes
  print(f'{dimes} dimes')


dimes_remainder = quarters_remainder % final_dimes
print(f'{dimes_remainder} pennies')