import java.util.ArrayList;
import java.util.Scanner;
public class EmployeePayroll {

	public static void main(String[] args){
	Scanner input = new Scanner(System.in);

	EmployeePayrollSystem pay = new EmployeePayrollSystem();

	String payroll = """
				Welcome to Semicolon Pay-roll
				press;-
				1. Add employee's pay-roll.
				2. View employee's pay-roll.
				3. Update employee's pay-roll.
						4. Exit.
				""";
	boolean payRollView = true;
	while (payRollView == true){

	System.out.print(payroll);
	System.out.print("Enter selection: ");
	int selection = input.nextInt();

	switch (selection){
		case 1: {
				boolean addPayroll = true;
				while (addPayroll == true){
					System.out.print("Enter employee's name: ");
					String employeeName = input.nextLine();
					
					System.out.print("Number of work hours per week: ");
					double workHours = input.nextDouble();

					System.out.print("Enter hourly pay-rate: ");
					double payRate = input.nextDouble();

					System.out.print("Enter federal withholding tax rate: ");
					double federalTaxRate = input.nextDouble();

					System.out.print("Enter state withholding tax rate: ");
					double stateTaxRate = input.nextDouble();

					pay.payRoll(employeeName, workHours, payRate, federalTaxRate, stateTaxRate);

					addPayroll = false;
					} break;
				}

		case 2: {
				boolean viewPayroll = true;
				while (viewPayroll == true){
					System.out.print("Enter employee's name: ");
					String employeeName = input.nextLine();
					}
				}
		case 3:{
				

				}
		case 4: {
				System.out.print("Good-Bye...");
				payRollView = false;
				} break;
		default : {
				System.out.print("Enter a valid option");
				payRollView = true;
				}
	}

	}
	}

}