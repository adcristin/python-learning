#Building a simple even/odd checker using if-condition. 

n = int(input("Enter your desired integer to check whether it's even or odd: "))

if(n%2 == 0):
    print(n, "is a even number.")
elif(n%2 != 0):
    print(n, "is a odd number.")
else:
    print("INVALID")
    