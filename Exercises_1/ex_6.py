# Perfect number if it is equal to the sum of all its divisors


def perfect_number(n):
  is_perfect = " is not a perfect number"
  sum = 0

  if n == 1 :
     is_perfect = " is a perfect number"
  
  for i in range(1, n//2 + 1):
      if n % i == 0: 
        sum +=i
      
      if sum == n:
        is_perfect = " is a perfect number"
    


  return   str(n) + is_perfect



print( perfect_number(6) )
print( perfect_number(28) )
print( perfect_number(8) )
print( perfect_number(1) )

