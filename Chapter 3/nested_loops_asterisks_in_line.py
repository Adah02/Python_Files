print(f'(a) \t    (b) \t  (c)   \t (d)')
for i in range(1, 11):
  print(f'{'*' * i:<12}{'*' * (11 - i):12}{'*' * (11 - i):>12}{'*' * i:>12}')