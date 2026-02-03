'''
Question:

Reverse a string.
'''

string = str(input("Enter a string to be reversed : "))
rev = ""

for ch in string:
    rev = ch + rev

print(rev)


    
