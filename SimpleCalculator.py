#We'll make a simple calculator with the use of if-condtion statement. 

print("-------------------------CALCULATOR---------------------------")

print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")

print("--------------------------------------------------------------")

number = int(input("Enter your chosen operation's number : "))

print("--------------------------------------------------------------")

if(number<=4):
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    if(number == 1):
        print("Addition is: ", a+b)
    elif(number == 2):
        if(b>a):
            print("Subtraction is: ", b-a)
        else:
            print("Subtraction is: ", a-b)
    elif(number == 3):
        print("Multiplication is: ", a*b)
    elif(number == 4):
        if(a == 0 & b == 0):
            print("Divison is: 0")
        elif(b == 0):
            print("Undefined! Denominator is 0")
        elif(a == 0):
            print("Divison is: 0")
        else:
            print("Division is ", a/b)
    else:
        print("INVALID!")
else:
    print("INVALID CHOICE!")

       

