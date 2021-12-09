# Find the summation



def sum(n):
  output =""
  total = 0

  for i in range(n):
    total +=n
    if i < n-1:
      output += "{0} + ".format(n)
    else:
      output += str(n) +  ' = ' + str(total) 

  return output



print(sum(3))
print(sum(7))
