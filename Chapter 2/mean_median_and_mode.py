import statistics
number = (9, 11, 22, 34, 17, 22, 34, 22, 40, 34)

ascending_order_of_number = sorted(number)
mean_value = statistics.mean(ascending_order_of_number)
median_value = statistics.median(ascending_order_of_number)
mode_value = statistics.mode(ascending_order_of_number)

print(f'{mean_value:>.1f} {median_value:>.1f} {mode_value:>.0f}')
print(ascending_order_of_number)