#Set comprehension is a concise and efficient way in Python to create sets from iterables(like lists, tuples, or strings) using a single, readable line of code.

names = {'apple', 'orange', 'mango', 'watermelon', 'pineapple'}

names2 = {element.capitalize() for element in names}
print("Fruits : ", names2)
