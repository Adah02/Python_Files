number_of_students = int(input('Enter number of students: '))
student_score = 0
highest_score = 0
second_highest_score = 0

for index in range(number_of_students):
  student_score = int(input('Enter student\'s score: '))
  student_name = str(input('Enter student\'s name: '))
    
  if student_score > highest_score:
    highest_score = student_score
    name = student_name
  elif student_score > second_highest_score:
    second_highest_score = student_score
    name2 = student_name


print(name,'has',highest_score)
print(name2,'has',second_highest_score)
 