#Array of student scores.
#This is referred to as 'List' in python. And it can contain different data types.

scores = [50,34,45,50,25]

cart = ['plantain', 33, 'juice', 2.5, ['fish', 'palm oil'], True]

print(f'We have {len(cart)} items in your cart')
print(cart[4])

print(f'We have {len(scores)} scores for prim {len(scores) - 2}')

for items in scores:
  print(items)

counter = 0
for item in cart:
  print(f'index {counter} = {item}')
  counter += 1

#Printing multiple items from  in the same line.

print(cart[1:55])

for value in enumerate(cart):
  print(value)


scores.append(67)
scores.pop(3)
cart[4].insert(0, 8)
scores.extend([34,67,87,65])

#(+ and *) are regarded as overloaded operators.

print(scores)

print(cart[0].upper())

print(scores[len(scores) : 0:-1])
print(scores[::2])

new_list = cart + scores
print(new_list)
