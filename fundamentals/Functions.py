#Functions in Python are named blocks of reusable code that perform a specific task, helping to organize programs, improve readability, and prevent code repetition. They are defined using the def keyword. 

#Calculating circumference of a circle with different-different radius.
import math

def CircumferenceOfCircle(radius):
    return 2*math.pi*radius #the return statement is used inside a function to terminate its execution and send a value back to the caller. This value can then be used in other parts of the program, such as being assigned to a variable or used in an expression. 

R1 = int(input("Enter the radius of circle 1: "))
R2 = int(input("Enter the radius of circle 2: "))
R3 = int(input("Enter the radius of circle 3: "))

print()

print("Circumference of circle 1: ", CircumferenceOfCircle(R1))
print("Circumference of circle 2: ", CircumferenceOfCircle(R2))
print("Circumference of circle 3: ", CircumferenceOfCircle(R3))

