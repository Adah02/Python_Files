import java.util.ArrayList;
public class EmployeePayrollSystem {

	public static double payRoll (String employeeName, double workHours, double payRate, double federalTaxRate, double stateTaxRate){

		ArrayList <double> semicolonPayroll = new ArrayList <> ();

		double grossPay = payRate * workHours;
		final double P	ERCENTAGE = 100;
		double federalWithholding = (grossPay / PERCENTAGE) * federalTaxRate;
		double stateWithholding = (grossPay / PERCENTAGE) * stateTaxRate;
		double totalDeduction = federalWithholding + stateWithholding;
		double netPayment = grossPay - totalDeduction;
		
	}
}