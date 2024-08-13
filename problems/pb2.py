# declare and fill out function here
def max_values(l):
  max = l[0]
  for i in l:
    if i > max:
     max = i
    for j in l:
      if j > max & j != max:
        max2 = j
  return l.index(max), l.index(max2)
# test case
print(max_values2([-5, -2, -1, -11])) # -> [1, 2]
