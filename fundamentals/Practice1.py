'''
Question: 

Swap two numbers without using a third variable.
'''

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("Before Swapping:", num1,",", num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2 

print("After Swapping:", num1,",",  num2)



