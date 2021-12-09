# Palindrome  Strings


def palindrome(input_str):
    if input_str == input_str[::-1]:
        return True
    else:
        return False

# print( palindrome("abcba") )
# print( palindrome("catac") )
# print( palindrome("Soos") )
# print( palindrome("kihhik") )


def max_sub_palindrome(input_str):
    output= []
   
    for i in range( len(input_str) ):
        for j in range(i):
            if palindrome(  input_str[j:i+1] ):
                 output.append( input_str[j:i+1] )

    max = 0
    if len(output) == 0:
        final_palindrome = input_str[:1]
        
    for i in output:
        if  len(i) > max:
            max = len(i)
            final_palindrome = i
    return final_palindrome


print( max_sub_palindrome("aaabaaac") )
print(  max_sub_palindrome("abe") )
print(  max_sub_palindrome("ccABBAd") )
print(  max_sub_palindrome("XYZZYX") )

