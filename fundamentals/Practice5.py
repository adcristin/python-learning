'''
Question:

Checking whether a number is palindrome or not. 
'''

num = int(input("Enter a number: "))
original = num
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
Question:

Checking whether a number is armstrong or not. 
'''

digits = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total += digit ** digits
    num //= 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
    