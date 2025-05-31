total_miles_driven = 0
total_gallons_per_tank = 0

miles_driven = 0
gallon_per_tank = 0

while miles_driven != -1 or gallon_per_tank != -1:
  total_miles_driven += miles_driven
  total_gallons_per_tank += gallon_per_tank
  miles_driven = int(input('Enter miles driven. type -1 to stop: '))
  gallon_per_tank = int(input('Enter gallons per tank. type -1 to stop: '))

average_miles_per_gallon = total_miles_driven / total_gallons_per_tank

print(f'The average miles per gallon is {average_miles_per_gallon:>.2f}')