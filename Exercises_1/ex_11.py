# Co-prime numbers have no common integer divisors other than the integer 1


def coprime(a, b):

    if a == b:
        return False
    if a == 1 or b == 1:
        return True
    if a % b == 0 or b % a == 0:
        return False

    for i in range(2, a // 2):
        if a % i == 0 and b % i == 0:
                return False

    return True


# print( coprime(12, 25) )
# print( coprime(12, 100) )
# print( coprime(12, 1) )
# print( coprime(1, 100) )
# print( coprime(3, 3) )
# print( coprime(2, 4) )
# print( coprime(86, 2) )


def count_coprimes(n):
    count = 0
    
    for i in range(1, n):
        if  n % i != 0 : 
            if coprime(n, i):
                count += 1

    return count+1


print(count_coprimes(25))
print(count_coprimes(4))
print(count_coprimes(12))
print(count_coprimes(86))
