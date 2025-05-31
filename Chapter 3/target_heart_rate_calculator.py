age = int(input('Enter your age: '))

percentage_target_rate = 60
percentageconstant = 100
actual_rate = percentage_target_rate / percentageconstant

target_heart_rate = int((220 - age) * actual_rate)
maximum_heart_rate = 220 - age

print('Your maximum heart rate is',maximum_heart_rate,'bpm')
print('Your target heart rate at 60% is',target_heart_rate,'bpm')