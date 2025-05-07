print('Enter radius of the circle')
radius = input()

pi = 3.14159

diameter = pi * float(radius)
circumference = 2 * pi * float(radius)
area = pi * (float(radius)**(2))

print('The diameter is ',diameter, '\nThe circumference is ', circumference, '\nThe area is ', area)