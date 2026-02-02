'''
Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.

How it works:

1.Go through the array, one value at a time.
2.For each value, compare the value with the next value.
3.If the value is higher than the next one, swap the values so that the highest value comes last.
4.Go through the array as many times as there are values in the array.
'''

def BubbleSort(arr, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

length = int(input("Enter the length of your array: "))
myArray = []
for i in range(length):
    element = int(input("Enter the element you want to add: "))
    myArray.append(element)
print("\nArray Before Sorting :", myArray)

result = BubbleSort(myArray, length)
print("Array After Sorting :", result)