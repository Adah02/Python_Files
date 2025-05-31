total = int(input('Enter total purchase amount: '))

final_percentage = 100

if total >= 1000 & total <= 10000:
  discount_percentage = 5
  discount = total * (discount_percentage / final_percentage)
  payment_amount = total - discount
  print(f'Your discount amount is {discount:,}')
  print(f'Your payment amount is {payment_amount:,}')

elif total > 10000 & total <= 50000:
  discount_percentage = 10
  discount = total * (discount_percentage / final_percentage)
  payment_amount = total - discount
  print(f'Your discount amount is {discount:,}')
  print(f'Your payment amount is {payment_amount:,}')

elif total > 50000:
  discount_percentage = 20
  discount = total * (discount_percentage / final_percentage)
  payment_amount = total - discount
  print(f'Your discount amount is {discount:,}')
  print(f'Your payment amount is {payment_amount:,}')
