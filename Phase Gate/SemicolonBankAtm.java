import java.util.Scanner;
public class SemicolonBankAtm {

	public static void main(String[] args){

	Scanner input = new Scanner(System.in);

	SemicolonBankAtmFile atm = new SemicolonBankAtmFile();

	System.out.println("Welcome to Semicolon ATM");

	System.out.print("Enter balance: ");
	double balance = input.nextDouble();
	while (balance < 1){
		System.out.print("Enter a valid balance: ");
		balance = input.nextDouble();
		}

	System.out.print("Enter withdrawal amount in multiples of 500 or 1000: ");
	double withdrawalAmount = input.nextDouble();

	atm.accountBalance(balance);

	atm.accountWithdrawal(withdrawalAmount, balance);

	}
}