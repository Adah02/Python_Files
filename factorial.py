userinput = int(input('Enter an integer: '))

factorial = 1
for userinput in range(1, userinput +1):
  factorial *= userinput

print(f'The factorial of {userinput} is {factorial}')
