# Find sum recursively

def recursive_sum(n):
    if n == 1:
        return 1
    elif n > 1:
        return  n + recursive_sum(n-1)
    else:
        print("Enter only  numbers > 1")
        return n


print( recursive_sum(6) )
print( recursive_sum(1) )
print( recursive_sum(0) )
print( recursive_sum(-5) )