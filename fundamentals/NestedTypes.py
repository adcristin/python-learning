#Storing different containers into a one single container and assigning it to a variable. - Nested Types

alphabet = 'A'
counting = 1

alphabet = 'B'
counting = 2

alphabet = 'C'
counting = 3

First = ['A', 1]
Second = ['B', 2]
Third = ['C', 3]

Serial = [
    ['A', 1],
    ['B', 2],
    ['C', 3]
]

print(Serial)
print(Serial[0])
print(Serial[0][1])
Serial.append(['D', 4])
print(Serial)

#Just like lists nested type, we can create the same for tuples, dictionaries and sets too.

#Processing Nested Types with loop. 
for alphabet, counting in Serial:
    print("Alphabet: ", alphabet)
    print("Counting: ", counting)
    print("\n")

