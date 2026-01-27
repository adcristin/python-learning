'''
Question:

Find Factorial of a number.
'''
def factorial(n):
    if n < 0:
        return "INVALID"
    
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    
    return fact


num = int(input("Enter a number to calculate its factorial: "))
result = factorial(num)

print("Factorial of", num, "is:", result)

        