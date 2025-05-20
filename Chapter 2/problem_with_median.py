import statistics
number = str(input("Enter numbers separated with commas': "))

ascending_values = sorted(number)
median_value = statistics.median(ascending_values)

print(median_value)