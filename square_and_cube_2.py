print('number \tsquare \t cube')
for number in range(6):
  square = number**(2)
  cube = number**(3)
  print(f'{number:>6}\t{square:>6}\t{cube:>5}')
