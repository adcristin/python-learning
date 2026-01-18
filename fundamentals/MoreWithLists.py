#Lists are type of containers which can store numbers, strings, etc., within a square bracket. 

list1 = ["a", "b", "c", "d", "e"]

#Checking whether a element is present in the list with the help of 'in' and 'not in' keywords. They return in boolean values.
print("a" in list1) 
print("d" not in list1)
print("f" in list1)

#Finding the length of the list, using len().
print(len(list1))

#Adding a element in the end using append().
list1.append("f")
print(list1)

#Adding another list using extend().
list2 = [1, 2, 3, 4, 5, 6]
list1.extend(list2)
print(list1)

#Inserting an element at a desired position with index feature by using insert().
list2.insert(0, 0)
print(list2)

#Finding index/position of a specific element using index().
print(list1.index(4))

#Sorting a list - ascending or descending using sort().
list2.sort(reverse=True)
print(list2)

#Finding maximum or minimum element in the list using - max() & min().
print(max(list2), min(list2))

#Finding occurences of a specific element using count().
print(list1.count(0)) #o/p will be 0 because the element was inserted after the appending of list.0 wasn't their previously.

#Poping the last element of the list using pop().
print(list2.pop())

#Removing a element using remove(). NOTE: IF THERE ARE MORE THAN ONE OCCURANCE OF THE ELEMENT, IT WILL REMOVE THE FIRST ONE. 
list1.remove('a')
print(list1)

#Deleting the entire data of the list using clear(). NOTE: ONLY THE DATA WILL BE DELETED, LIST WILL EXIST.
list2.clear()
print(list2)

#Reversing the list(no sorting) using reverse().
list1.reverse()
print(list1)








