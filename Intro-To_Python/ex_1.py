# Implement a function that takes two integers as a parameter and returs a string with the sum of the two numbers.

def calculate_sum(a,b):
      sum=a+b
      return ('{0} + {1} = {2}'.format(a, b, sum))

print(calculate_sum(3,4))