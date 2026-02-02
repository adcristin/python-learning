'''
The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first breaking it down into smaller arrays, and then building the array back together the correct way so that it is sorted.

How it works:

1.Divide the unsorted array into two sub-arrays, half the size of the original.
2.Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
3.Merge two sub-arrays together by always putting the lowest value first.
4.Keep merging until there are no sub-arrays left.
'''

def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = MergeSort(left)
    right = MergeSort(right)

    return Merge(left, right)

def Merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

length = int(input("Enter the length of your array: "))
myArray = []
for i in range(length):
    element = int(input("Enter the element you want to add: "))
    myArray.append(element)
print("\nArray Before Sorting :", myArray)

print("Array After Sorting : ", MergeSort(myArray))