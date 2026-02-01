'''
The Binary Search algorithm searches through a sorted array and returns the index of the value it searches for.

How it works:

1. Check the value in the center of the array.
2. If the target value is lower, search the left half of the array. If the target value is higher, search the right half.
3. Continue step 1 and 2 for the new reduced part of the array until the target value is found or until the search area is empty.
4. If the value is found, return the target value index. If the target value is not found, return -1.
'''

def BinarySearch(targetVal, arr):
    left = 0 
    right = len(arr)-1

    while left <= right:
        mid = (left+right)//2
        
        if arr[mid] == targetVal:
            return mid
        elif arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

SortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Value = int(input("Enter the value you want to search: "))

result = BinarySearch(Value, SortedArray)

if result != 1:
    print("Element found at position: ", result)
else:
    print("Not found")

