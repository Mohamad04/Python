# Reverse a number recursively


# reverse = 0
# def  reverse_digits(n):
#     global reverse

#     if n > 0:
#         ones = n % 10
#         reverse = reverse * 10 + ones
#         n = reverse_digits( n//10 )
#         return reverse
    


def reverse_digits(n, ones = 0):
    if n == 0:
        return ones
    else:
         return reverse_digits(n//10, ones * 10 + n % 10)


print( reverse_digits(1) )
print( reverse_digits(0) )
print( reverse_digits(29) )
print( reverse_digits(456) )