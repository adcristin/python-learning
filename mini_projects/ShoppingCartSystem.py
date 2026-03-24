#Building a simple shopping cart system where user can 'add items', 'remove items', 'total bill calculation' & 'apply discount'.

items = {
    'phone': 20000,
    'charger': 1500,
    'phonecase': 500,
    'earphones': 1000,
    'screenguard': 200
}

cart = {}  # stores items added by user

while True:
    print("\nWELCOME TO YOUR SHOPPING CART!")
    print("--------------------------------")
    print("1. Add Items")
    print("2. Remove Items")
    print("3. Total Bill")
    print("4. Apply Discount")
    print("5. Exit")
    print("--------------------------------")

    choice = int(input("Enter your chosen action number: "))

    # Add Items
    if choice == 1:
        item = input("Enter item name: ").lower()

        if item in items:
            qty = int(input("Enter quantity: "))
            
            if item in cart:
                cart[item] += qty
            else:
                cart[item] = qty

            print("Item added to cart.")
        else:
            print("Item not available.")

    # Remove Items
    elif choice == 2:
        item = input("Enter item to remove: ").lower()

        if item in cart:
            del cart[item]
            print("Item removed from cart.")
        else:
            print("Item not in cart.")

    # Total Bill
    elif choice == 3:
        total = 0
        print("\nYour Cart:")
        for item, qty in cart.items():
            price = items[item] * qty
            print(item, "x", qty, "=", price)
            total += price

        print("Total Bill:", total)

    # Apply Discount
    elif choice == 4:
        total = 0
        for item, qty in cart.items():
            total += items[item] * qty

        if total > 5000:
            discount = total * 0.1  # 10% discount
            total -= discount
            print("Discount Applied: 10%")
        else:
            print("No discount applied (min purchase 5000).")

        print("Final Amount:", total)

    # Exit
    elif choice == 5:
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice!")
