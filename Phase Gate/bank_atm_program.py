while True:
	def deposit(deposit_amount):
		if deposit_amount > 0:
			balance += deposit_amount
		else:
			print('Enter a valid amount')
			deposit_amount = True
		return balance
			
	def account_balance(balance):
		if balance > 0:
			balance = balance
			return balance
		else:
			print('Enter a valid amount')
			balance = True


	def withdrawal(withdrawal_amount, balance):
		PERCENTAGE = 100
		withdrawal_percentage = (balance / PERCENTAGE ) * 90;
		if withdrawal_amount % 500 == 0 & withdrawal_amount % 1000 == 0:
			if withdrawal_amount > 0 and withdrawal_amount <= withdrawal_percentage:
				transaction_fee = 100
				actual_withdrawal = (withdrawal_amount + transaction_fee)
				balance -= actual_withdrawal
				print('Transaction Successful')
				print(f'Withdrawal amount: {withdrawal_amount:.2f}\n Transaction Fee: {transaction_fee:.2f} \n Current balance: {balance:.2f}')
				transaction_history.append(balance)
				return balance
			else:
				print('Invalid amount. Only 90% of your balance is permitted for withdrawal')
				withdrawal_amount = True
		else:
			print('Enter amount that is a multiple of 500 or 1000')
			withdrawal_amount = True

	transaction_history = [];
	withdrawal_amount = 0;
	print('Welcome to Semicolon Bank ATM')	
	balance = float(input('Enter your balance: '))
	
	while balance > 0:
		withdrawal_amount = True
		withdrawal_amount = int(input('Enter withdrawal amunt in multiples of 500 or 1000: '))
		print(withdrawal(withdrawal_amount, balance))

		print('''
		press 
		1 > Yes
		2 > No
		3 > Transaction History
		'''
		)
		userchoice = int(input('Would you like to perform another transaction? : '))
		match userchoice:
			case 1:
				withdrawal_amount = True
			case 2:
				balance = False
				break
			case 3:
				print('Balance after withdrawal :',transaction_history)
			case _: 
				balance = False
				break

	break
	

	






