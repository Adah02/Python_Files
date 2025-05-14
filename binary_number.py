binary_number = int(input('Enter a binary number: '))
number = binary_number

binary = 0
count = 0
while binary_number != 0:
  remainder = binary_number % 10
  binary += remainder * (2**(count))
  count += 1
  binary_number = binary_number // 10

print(number,'to base ten is',binary)