score1 = int(input('Enter integer: '))
score2 = int(input('Enter integer: '))
score3 = int(input('Enter integer: '))

minimum = min(score1, score2, score3)
maximum = max(score1, score2, score3)
ascending = 0

if score1 > minimum & score1 < maximum: ascending = score1
elif score2 > maximum & score2 < maximum: ascending = score2
elif score3 > maximum & score3 < maximum: ascending = score3
print(minimum, ascending, maximum)

