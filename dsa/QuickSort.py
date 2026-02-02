'''
The Quicksort algorithm takes an array of values, chooses one of the values as the 'pivot' element, and moves the other values so that lower values are on the left of the pivot element, and higher values are on the right of it.

How it works:

1.Choose a value in the array to be the pivot element.
2.Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
3.Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
4.Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.
'''

def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]

    left = [i for i in arr[:-1] if i <= pivot]
    right = [i for i in arr[:-1] if i > pivot]

    left = QuickSort(left)
    right = QuickSort(right)

    return left + [pivot] + right

length = int(input("Enter the length of your array: "))
myArray = []
for i in range(length):
    element = int(input("Enter the element you want to add: "))
    myArray.append(element)
print("\nArray Before Sorting :", myArray)

print("Array After Sorting : ", QuickSort(myArray))