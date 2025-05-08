print('Enter an integer of five-digits: ')
integer = int(input())

integer1 = integer // 10000
integer2 = integer // 1000 % 10
integer3 = integer // 100 % 10
integer4 = integer // 10 % 10
integer5 = integer % 10 

reverse = integer1 * 1 + integer2 * 10 + integer3 * 100 + integer4 * 1000 + integer5 * 10000

if(integer == reverse): print(integer," is a palindrome")
else: print(integer," is not a palindrome")
	

