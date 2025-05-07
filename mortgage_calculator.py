print('Enter principal amount: ') 
principalamount = int(input())

print('Enter annual percentage rate: ') 
annualpercentagerate = int(input())

print('Enter duration in years: ')
duration = int(input())

constantpercentage = 100
durationinmonths = duration * 12
actualrate = (annualpercentagerate / constantpercentage)

annualinterestrate = principalamount * (actualrate * ((1 + actualrate)**duration))

actualrateandyears = ((1 + actualrate)**duration) - 1

mortgage = (annualinterestrate / actualrateandyears)

monthsperyear = 12

monthlypayment = (mortgage + principalamount) / (duration * 12)

print(mortgage + principalamount)

print('Your monthly payment is ',monthlypayment)