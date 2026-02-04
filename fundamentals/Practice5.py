'''
Question:

Checking whether a number is palindrome or not. 
'''

num = int(input("Enter a number: "))
l = 0
s = 0
original = num
'''
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if reverse == original:
    print("Palindrome number")
else:
    print("Not a palindrome number")

'''
'''
Question:

Checking whether a number is armstrong or not. 
'''
n = num 

while n > 0:
    digit = n % 10
    n //= 10
    l += 1

while num > 0:
    digit = num % 10
    num //= 10
    s += digit**l

if s == original:
    print("Its an Armstrong number")
else:
    print("Not an Armstrong number")
    