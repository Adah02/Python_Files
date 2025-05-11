userinput = int(input('Enter integers: '))

sum = 0
multiple = 1

for i in range(1, 4+1):
  print(i)
  for j in range(1, i):
    multiple *= j
    print(j)
    sum += 1 / multiple

print(sum) 