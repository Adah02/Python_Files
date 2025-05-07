print('Enter an integer of five-digits: ')
integers = int(input())

integer1 = integers // 10000
integer2 = integers // 1000 % 10
integer3 = integers // 100 % 10
integer4 = integers // 10 % 10
integer5 = integers % 10 

reverse = integer5, integer4, integer3, integer2, integer1

print(reverse)

if(integers == reverse): print(integers, " is a palindrome")
else: print(integers,  " is not a palindrome")
	

