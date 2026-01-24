#A list comprehension is a concise and elegant way in Python to create a new list by applying an expression to each item in an existing iterable, optionally filtering the items based on a condition, all within a single line of code. 

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Traditional way:

EvenNums = []
for elements in nums:
    if(elements%2 == 0):
        EvenNums.append(elements)
print("Even Numbers in the 'Numbers' list : ", EvenNums)

#List Comprehension:

EvenNums2 = [elements for elements in nums if(elements%2 == 0)] #It reduces the LOC, if you use it in this way. 
print("Even Numbers in the 'Numbers' list : ", EvenNums2)