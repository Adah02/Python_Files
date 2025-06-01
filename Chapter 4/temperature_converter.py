def temperature(celcius):
	fahrenheit =  (9 / 5) * celcius + 32;
	return fahrenheit;

celcius = float(input('Enter temperature in degree celcius: '));
print(f'{temperature(celcius):.1f}');