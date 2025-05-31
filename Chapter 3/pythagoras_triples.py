for a in range(1, 20):
  for b in range(1, 20):
    a_b_square = ((a**(2)) + (b**(2)))
    for c in range(1, 20):
      if a_b_square == (c**(2)):
        print(a,',',b,'and',c)