passes = 0
failures = 0
userinput = 0

while userinput != -1:
  if userinput == 1:
    passes += 1
  if userinput == 2:
    failures += 1
  userinput = int(input('Enter 1 for pass or 2 for fail. type -1 to stop: '))

print(f'Your passes are {passes} and failures is {failures}')