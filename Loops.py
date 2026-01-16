# We'll implement loops : while and for.

start = int(input("Enter the minimum range: "))
limit = int(input("Enter the maximum range: "))

# while: We use it when we're not aware of how many times we need to run the loop.
number = start
while number <= limit:
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")
    number += 1

print("-------------------------------------------------")

# for: We use it when we're aware of how many times we need to run the loop.
for i in range(start, limit + 1):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")



        
    