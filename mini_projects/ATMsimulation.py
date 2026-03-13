balance = 10000
OriginalPin = 1900

pin = int(input("Enter your PIN: "))

if pin == OriginalPin:

    while True:

        print("\n-------------------- ATM Simulation --------------------")
        print("1. Balance Check")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("--------------------------------------------------------")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your current balance is:", balance)

        elif choice == 2:
            dep = int(input("Enter amount to deposit: "))
            balance += dep
            print("Deposit successful.")
            print("Updated balance:", balance)

        elif choice == 3:
            wit = int(input("Enter amount to withdraw: "))
            if wit > balance:
                print("Insufficient balance!")
            else:
                balance -= wit
                print("Please collect your cash.")
                print("Remaining balance:", balance)

        elif choice == 4:
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Incorrect PIN. Access denied.")
