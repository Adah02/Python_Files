user_input = int(input("Enter the integer of choice: "))

sum = 0
while user_input != 0: 
  remainder = user_input % 10
  sum += remainder
  user_input = user_input // 10

print(sum)