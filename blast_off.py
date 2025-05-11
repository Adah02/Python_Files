userinput = int(input('Enter input: '))
  
for index in range(userinput, 0, -1):
  if userinput < 1: 
    userinput = int(input('Enter number that is > 0r = 1: '))
  if index == 1:
    print('Blast off')
    break 
  print(index)
