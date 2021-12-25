


#2 Question   write a program that guess the user's number


import random

def guess_computer(x):
    low = 1
    high = x
    feedback = ""
    
    while feedback != "c":
        if  high > low :
            guess = random.randint(low,high)

        elif (guess == low+1 and guess == high -1) or low==high or low > high:
            guess = low
            break
            
        feedback = input(f"Is {guess} too High(H), too Lower(L), or  correct(c) ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yaaay the computer guessed your number :  {guess}, correctly 😁")




guess_computer(10)
         