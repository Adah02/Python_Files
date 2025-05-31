number_of_students = int(input('Enter number of students: '))
highest_score = 0

for index in range(number_of_students):
  student_score = int(input('Enter student\'s score: '))
  student_name = str(input('Enter student\'s name: '))
    
  if student_score > highest_score:
    highest_score = student_score
    name = student_name

print(name,'scored the highest, which is',highest_score)

 