'''
A Hash Table is a data structure designed to be fast to work with. The reason Hash Tables are sometimes preferred instead of arrays or linked lists is because searching for, adding, and deleting data can be done really quickly, even for large amounts of data. With a Hash Table, finding "Bob" is done really fast because there is a way to go directly to where "Bob" is stored, using something called a hash function.

To get the idea of what a Hash Table is, let's try to build one from scratch, to store unique first names inside it.

We will build the Hash Table in 5 steps:

1.Create an empty list (it can also be a dictionary or a set).
2.Create a hash function.
3.Inserting an element using a hash function.
4.Looking up an element using a hash function.
5.Handling collisions.
'''
#Empty list
my_list = [None, None, None, None, None, None, None, None, None, None]

#Defining hash function
def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10

print("'Bob' has hash code:", hash_function('Bob'))

#Inserting element using hash function
def add(name):
  index = hash_function(name)
  my_list[index] = name

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
print(my_list)

#Checking for the element using hash function
def contains(name):
  index = hash_function(name)
  return my_list[index] == name

print("'Pete' is in the Hash Table:", contains('Pete'))

#Collision handling 
my_list = [
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  []
]

def add(name):
  index = hash_function(name)
  my_list[index].append(name)

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Stuart')
print(my_list)
