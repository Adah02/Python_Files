sum = 1

for i in range(11, 1, -1):
  multiple = 1
  for j in range(1, i):
    multiple *= j
  sum += 1 / multiple

print(sum) 