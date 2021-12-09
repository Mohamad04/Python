# Implement a function that takes a positive number n as parameter, and returns the sum of odd integers less than or equal to n



def odd_sum(n):
  total = 0
  for i in range(n+1):
    if (i % 2 != 0):
      total+=i

  return total 


print(odd_sum(9))
print(odd_sum(6))
print(odd_sum(21))
print(odd_sum(0))