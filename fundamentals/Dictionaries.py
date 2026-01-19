#We'll see what are dictionaries: Dictionaries are also containers but they store elements in the form of {'key': 'value'}. 

dic1 = {1: 'A', 2: 'B', 3: 'C'}

dic1[4] = 'D' #this pair will get inserted in the dictionary. 
print(dic1)

dic1.update({5: 'E', 6: 'F'}) #these pairs will get inserted in the dictionary.
print(dic1)

del(dic1[6]) #to delete pair 
print(dic1)

dic1.pop(5) #to delete pair too
print(dic1)

dic1.popitem() #to delete the last pair 
print(dic1)

print(len(dic1)) #length of the dictionary

dic1.clear() #to delete entire data from the dictionary
print(dic1)