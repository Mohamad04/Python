# Write a function that takes two positive numbers as parameters and return True if the second number is the square root of the first number and False otherwise

def is_square_root(x,y):
  if y*y == x:
    return "True"
  else: 
    return "False"

 

print( is_square_root(4, 1))
print( is_square_root(16, 4))
print( is_square_root(84, 6))