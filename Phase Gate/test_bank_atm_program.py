import bank_atm_program
from unittest import TestCase

class test_for_account_transactions(TestCase):

	def test_for_account_balance(self):
		check =  bank_atm_program.account_balance(4000)
		expected = 4000.00

		self.assertEqual(check, expected)

	def test_for_withdrawal(self): 
		check = bank_atm_program.withdrawal(3000, 10000)
		expected = 6900.00

		self.assertEqual(check, expected)
	
	def test_for_invalid_withdrawal(self): 
		check = bank_atm_program.withdrawal(10000, 10000)
		expected = ''

		self.assertEqual(check, expected)

	def test_for_invalid_withdrawal(self): 
		check = bank_atm_program.withdrawal(300, 10000)
		expected = ''

		self.assertEqual(check, expected)
