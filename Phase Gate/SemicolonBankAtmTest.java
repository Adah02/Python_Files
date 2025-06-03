import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class SemicolonBankAtmTest {

	SemicolonBankAtmFile atm = new SemicolonBankAtmFile();

	@Test
	public void accountBalanceCheck(){
	int check = 1000;
	int expected = 1000;

	assertEquals(atm.accountBalance(check), expected);
	}

	@Test
	public void withdrawalCheck(){
	double balance = 10000;
	double withdrawal = 1000;
	double expected = 8900.00;

	assertEquals(atm.accountWithdrawal(withdrawal, balance), expected);
	}

}