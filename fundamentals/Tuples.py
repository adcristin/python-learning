#We'll see what are tuples: Tuples are also sort of containers like Lists, but they are represented in () and are immutable.

tup = (1, 2, 3, 4, 5)
print(tup)

#If we try to modify/update or insert any element then we can't do that because it is immutable.
tup.insert(0, 0) #We get an error

#But, we can access elements through indexing. 
print(tup[0])