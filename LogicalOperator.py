#There are several logicial operators such as: AND, OR & NOT. They give BOOLEAN values. 

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if(a > 0 and b > 0): #AND : True, when all conditions are true.
    print("Both are positive values")
elif(a > 0 or b > 0): #OR : True, even if one condition is true.
    print("Only one of them is a positive value")
elif(not(a > 0 and b > 0)): #NOT : Inverse of the real condition outcome. 
    print("Both are negative values")
else:
    print("INVALID!")

