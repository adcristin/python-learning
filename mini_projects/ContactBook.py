#Building a Contact Book using dictionary and functions. 

contacts = {}

def add_contact():
    n = int(input("Enter the number of contacts you want to add : "))
    for i in range(n):
        name = input("Name : ")
        number = input("Number : ")
        contacts[name] = number
    print("Contact(s) added successfully!\n")


def search_contact():
    search = input("Enter the name of the contact you want to search : ")
    if search in contacts:
        print("Here's your searched contact :", search, "-", contacts[search])
    else:
        print("Sorry! The searched contact is not in the contact book.")
    print()


def delete_contact():
    delete = input("Enter the name of the contact you want to delete : ")
    if delete in contacts:
        del contacts[delete]  
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")
    print()


def display_contact():
    if contacts:
        print("Current Contact Book:")
        for name, number in contacts.items(): 
            print(name, ":", number)
    else:
        print("Contact book is empty.")
    print()

while True:
    print("WELCOME TO YOUR CONTACT BOOK!")
    print("---------------------------------")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contact")
    print("5. Exit")

    choice = int(input("Enter your chosen operation's number : "))

    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        delete_contact()
    elif choice == 4:
        display_contact()
    elif choice == 5:
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid Choice!\n")



