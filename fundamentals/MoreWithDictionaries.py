#We'll see how Nested Dictionaries works. 

people = {
    "A": {'id': 1, 'age': 18},
    "B": {'id': 2, 'age': 19},
    "C": {'id': 3, 'age': 20}
}

print(people)
print(people["A"])
print(people["A"]['age'])

#Accessing Nested Dictionary through loop.

for name, details in people.items():
    print("name:", name)
    print("id:", details["id"])
    print("age:", details["age"])
    print()

#User adding/searching/deleting in dictionaries:

dic = {}

while(True):

    print("1: Add a item in the dictionary")
    print("2: Search an item in the dicitionary")
    print("3: Delete an item from the dictionary")

    choice = int(input("Enter your desired operation you want to perform: "))

    if(choice == 1):
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        dic[key] = value
        print("Item added to the dictionary!\n")
    elif(choice == 2):
        key = input("Enter the item you want to search: ")
        if key in dic:
            print("Here's your searched item: ", key,"," ,dic[key])
            print()
        else:
            print("Item not found!\n")
    elif(choice == 3):
        key = input("Enter the item you want to delete: ")
        if key in dic:
            del dic[key]
            print("Item has been deleted!")
            print("Current dictionary: 4", dic)
            print()
        else:
            print("Item not found!\n")
    else:
        print("Invalid choice!\n")
    
    

