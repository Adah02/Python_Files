function account_balance(balance){
		balance = balance
		return balance
		};

function withdrawal(withdrawalAmount, balance){
		let percentage = 100
		let withdrawalPercentage = ((balance / percentage ) * 90);
		if (withdrawalAmount % 500 == 0 && withdrawalAmount % 1000 == 0){
			if (withdrawalAmount > 0 & withdrawalAmount <= withdrawalPercentage) {
				let transactionFee = 100;
				let actualWithdrawal = (withdrawalAmount + transactionFee)
				balance = balance - actualWithdrawal
				console.log("Transaction Successful")
				console.log("Withdrawal amount:",withdrawalAmount,"\nTransaction Fee: ",transactionFee,"\nCurrent balance: ",balance)
				return balance
				}else{
				console.log('Invalid amount. Only 90% of your balance is permitted for withdrawal')
				withdrawalAmount = True
				};
			return balance
			}
		else {
			console.log("Enter amount that is a multiple of 500 or 1000")
			withdrawalAmount = True
			};
		};

const prompt = require("prompt-sync")()

let balance = prompt('Enter balance: ')
let withdrawalAmount = prompt("Enter withdrawal amount: ")

console.log(withdrawal(withdrawalAmount, balance))



