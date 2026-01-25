import string

special_chars = string.punctuation

print("Password Constraints:")
print("- Minimum 8 characters")
print("- At least 1 special character")
print("- At least 1 uppercase letter")
print("- At least 1 lowercase letter")
print("- At least 1 digit")
print()

password = input("Enter your password: ")

has_special = False
has_upper = False
has_lower = False
has_digit = False

if len(password) >= 8:
    for ch in password:
        if ch in special_chars:
            has_special = True
        elif ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
    if has_special and has_upper and has_lower and has_digit:
        print("Password created successfully!")
    else:
        print("Password is missing some constraints.")
else:
    print("Password must be at least 8 characters long.")



