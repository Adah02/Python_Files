current_population = int(input('Enter current population: '))
growth_rate = float(input('Enter current growth rate: '))

final_percentage = 100
actual_rate = (growth_rate / final_percentage)
future_population = current_population * (1 + (actual_rate))
difference = future_population - current_population

for index in range(1, 100 + 1):
  print(f'{index} \t {future_population:>.0f}')
  future_population += difference
  