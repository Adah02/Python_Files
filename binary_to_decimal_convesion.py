binary_number = int(input('Enter the binary number: '))

binary = 0

for index in range(binary_number):
  remainder = binary_number % 10
  binary_calc = remainder * (2**(index))
  binary += binary_calc
  binary_number = binary_number // 10
  print(remainder)
print(binary)