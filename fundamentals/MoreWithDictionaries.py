#We'll see how Nested Dictionaries works. 

people = {
    "A": {'id': 1, 'age': 18},
    "B": {'id': 2, 'age': 19},
    "C": {'id': 3, 'age': 20}
}

print(people)
print(people["A"])
print(people["A"]['age'])

for name, details in people.items():
    print("name:", name)
    print("id:", details["id"])
    print("age:", details["age"])
    print()
