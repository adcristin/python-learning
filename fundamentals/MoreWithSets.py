#We'll see what operations we can perform on sets.

Set1 = {1, 2, 3, 4, 5}
Set2 = {3, 4, 5, 6, 7}

#Union - union()/'|'
print(Set1.union(Set2))
print(Set1 | Set2)

#Intersection - intersection()/'&'
print(Set1.intersection(Set2))
print(Set1 & Set2)

#Difference - difference()/'-'
print(Set1.difference(Set2))
print(Set1 - Set2)

#XOR(removing intersection from union) - '^'
print(Set1 ^ Set2)