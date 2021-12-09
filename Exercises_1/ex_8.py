#  write a function that counts the digits of a number recursively


def digits_recursive(n):
    if n == 0:
        return 0
    elif abs(n) < 10:
        return 1
    else:
        return 1 +  digits_recursive(n/10)



print(  digits_recursive(123) )
print(  digits_recursive(0) )