def employee_pay_roll(employee_name, work_hours, pay_rate, federal_tax_rate, state_tax_rate):
	#To calculate and prepare employee's payroll.
	gross_pay = pay_rate * work_hours;
	PERCENTAGE = 100;
	federal_withholding = ((gross_pay / PERCENTAGE) * federal_tax_rate)
	state_withholding = ((gross_pay / PERCENTAGE) * state_tax_rate)
	total_deduction = federal_withholding + state_withholding;
	net_pay = (gross_pay  - total_deduction)
	
	counter = 0
	while = True:
		payrolls += print(f'
			Employee name: {employee_name} \nWork hours: {work_hours} \nPay Rate: {pay_rate} \nGross Pay: {gross_pay} \nDeduction: \n\t Federal Withholding: {federal_withholding} \n\t State Withholding: {state_withholding} \nNet Pay: {net_pay}
		')
		print('Employee Pay-roll added =============>')
		counter += 1
	return payrolls
		


payrolls = []

payroll = """
			Welcome to Semicolon Pay-roll
			press;-
			1. Add employee's pay-roll.
			2. View employee's pay-roll.
			3. Update employee's pay-roll.
					4. Exit.
			"""
pay_roll_view = True
while pay_roll_view == True:
	print(payroll)
	selection = int(input("Enter selection: "));
	match selection:
		case 1: 
			add_payroll = True;
			while add_payroll == True:
				employee_name = str(input("Enter employee's name: "))
				work_hours = float(input("Number of work hours per week: "))
				pay_rate = float(input("Number of work hours per week: "))
				federal_tax_rate = float(input("Enter federal withholding tax rate: "))
				state_tax_rate = float(input("Enter federal withholding tax rate: "))
				add_payroll = false;
				break;
		case 2: 
			view_payroll = True
			while view_payroll == True:
				employee_name =input("Enter employee's name: ")
				for item in range(payrolls.length):
					if employee_name == item:
						
		case 3:
	
		case 4: 
			print("Good-Bye...")
			pay_roll_view = false
			break
		case _: 
			print("Enter a valid option");
			pay_roll_view = true;
				
