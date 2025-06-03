import java.util.Scanner;
public class SemicolonBankAtm {

	public static void main(String[] args){

	Scanner input = new Scanner(System.in);

	SemicolonBankAtmFile atm = new SemicolonBankAtmFile();

	System.out.print("Welcome to Semicolon ATM");
	double balance = input.nextDouble();
	while ()

	boolean withdrawal = true;
	System.out.print("Enter withdrawal amount in multiples of 500 or 1000: ");
	double withdrawalAmount = input.nextDouble();

	atm.accountBalance(balance);

	atm.accountWithdrawal(withdrawalAmount, balance);

	}
}