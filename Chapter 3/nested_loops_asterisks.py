print('a')
for i in range(1, 11):
  for j in range(1, i):
    print('*', end = '')
  print('')
print('\n')


print('b')
for i in range(11, 1, -1):
  for j in range(i, 1, -1):
    print('*', end = '')
  print('')
print('\n')


print('c')
for i in range(1, 11):
  for j in range(1, 11-i + 1):
    print('',end = ' ')
  for j in range(1, i,):
    print('*',end = '')
  print(' ')
print('\n')


print('d')
for d in range(11, 1, -1):
  for k in range(d, 1, -1):
    print('*',end = '')
  print('')