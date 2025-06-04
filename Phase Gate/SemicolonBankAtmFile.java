public class SemicolonBankAtmFile {

	private double balance;
	private double accountWithdrawal;
	
	public static double accountBalance(double balance){
		balance = balance;
	return balance;
	}
	
	public static double accountWithdrawal(double withdrawalAmount, double balance){
		final double PERCENTAGE = 100;
		double withdrawalPercentage = ((balance / PERCENTAGE) * 90);
		if (withdrawalAmount % 500 == 0 && withdrawalAmount % 1000 == 0){
			System.out.println("Withdrawal Percentage" + withdrawalPercentage);
			if (withdrawalAmount <= withdrawalPercentage && withdrawalAmount > 0){
				double withdrawalFee = 100;
				balance -= (withdrawalAmount + withdrawalFee);
				System.out.println("Transaction Successful");
				System.out.printf("Withdrawal amount: N%.2f%nWithdrawal Fee: N%.2f%n Remaining Balance: N%.2f%n", withdrawalAmount, withdrawalFee, balance);
			return balance;
			}
			else{
				System.out.print("Invalid amount. Only 90% of your balance is permitted for withdrawal");
				}
			}
		else{
			System.out.print("Withdrawal amount must be a multiple of 500 or 1000");
			}
		return balance;
		}
}
