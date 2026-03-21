#Building a simple email validator program where after user gives the email id, the program will check whether it contains '@', domain and no spaces or not. 

mail = input("Enter your email id: ")

if ("@" in mail and " " not in mail and mail.count("@") == 1):
    at_index = mail.index("@")

    if at_index > 0 and at_index < len(mail) - 1:
        domain_part = mail[at_index + 1:]

        if "." in domain_part:
            print("Valid Email ID!")
        else:
            print("Invalid Email ID!")

    else:
        print("Invalid Email ID!")
        
else:
    print("Invalid Email ID!")


    

    

