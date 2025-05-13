userinput = int(input('Enter integers: '))

sum = 1

for i in range(userinput + 1, 1, -1):
  multiple = 1
  for j in range(1, i):
    multiple *= j
  sum += 1 / multiple

print(sum) 