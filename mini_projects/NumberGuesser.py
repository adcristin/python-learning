#Building a simple number guessing game using while loop. 

SecretNum = 67

GuessNum = 0 

while(SecretNum != GuessNum):
    GuessNum = int(input("Guess the number: "))
    if(SecretNum == GuessNum):
        print("YOUR GUESS WAS CORRECT.", SecretNum, "was the secret number.")
    elif(SecretNum > GuessNum):
        print("OOPS!, the secret number is bit bigger. TRY AGAIN!")
    elif(SecretNum < GuessNum):
        print("OOPS!, the secret number is bit smaller. TRY AGAIN!")
    else:
        print("INVALID")





