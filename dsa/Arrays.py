#Arrays are fundamental, linear data structures that store a collection of elements of the same data type in contiguous memory locations.

arr = [1, 2, 3, 4, 5]

#Traversing:
for i in arr:
    print(i)

#Indexing:
print(arr[1])
print(arr[2])

#Length:
print(len(arr))

#Input:
n = int(input("Enter the number of elements you want to add in the array: "))
arr1 = []
for i in range(n):
    element = int(input("Enter the element you want to add: "))
    arr1.append(element)
print()
print("Your array: ", arr1)
