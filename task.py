import random 
import math
#take two numbers from user as upper and down 
lower = int(input("enter an lower number-: "))
upper = int(input("enter an upper number:- "))
# an random number generated b/t upper and lower number 
x = random.randint(lower,upper)
print("\n\tyou have", round(math.log(upper - lower + 1, 2)), "guesses only!\n" )

# initialising steps
count = 0 

# function properties
while count < math.log(upper - lower + 1,2):
    count += 1
    # take guess an output
    guess = int(input("guess an number:- "))
# conditional statement
    if x == guess:
        print("congratulations your guess is correct in ",
     count, "trials")
     # break statement if complete guess
     # once guessed loop will break
        break
    elif x > guess:
        print("your guess is too small!") 
    elif x < guess:
        print("your guess is too large!")
            
# when all guesse gets over then this conditions will executed

if count >= math.log(upper - lower + 1,2):    
    print("\n the number is %d" % x)   
    print("\t better luck next time! ")  
