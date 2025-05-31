binary_number = int(input('Enter a five digit the binary number: '))
number = binary_number

binary = 0
for index in range(5):
  remainder = binary_number % 10
  binary += remainder * (2**(index))
  binary_number = binary_number // 10

print(number,'to base ten is',binary)