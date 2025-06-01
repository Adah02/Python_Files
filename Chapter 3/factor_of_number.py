userinput = int(input('Enter an integer: '))
print(f'The factors of',userinput, 'are;')


i = userinput
for i in range(1, i +1):
  if userinput % i == 0:
    print(i, end= ' ')
