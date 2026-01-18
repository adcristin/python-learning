#Building a simple access control environment where if the given user is present in the specific name list, then and only then the user will be provided access. 

Users = ["Rohan", "Aryan", "Rahul", "Nitish", "Abhishek"]

UserName = input("Enter your name, to get access: ")

if UserName in Users:
    print("ACCESS GRANTED!")
else:
    print("ACCESS DENIED!")
