def temperature(celcius):
	fahrenheit =  (9 / 5) * celcius + 32;
	return fahrenheit;

print('Celcius \t fahrenheit')
#celcius = float(input('Enter temperature in degree celcius: '));
for celcius in range(1, 101, 1):
	print(f'{celcius} \t {temperature(celcius):.1f}');