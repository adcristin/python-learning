'''
Question:

Check whether input is positive, negative, or zero
'''
num = int(input("Enter a number to be checked whether its +ve/-ve/0 : "))

if num > 0:
    print(f'{num} is a positive number.')
elif num < 0:
    print(f'{num} is a negative number.')
elif num == 0:
    print(f'Number is zero.')
else:
    print("INVALID!")


