'''
Linear search (or sequential search) is the simplest search algorithm. It checks each element one by one.

How it works:

1. Go through the array value by value from the start.
2. Compare each value to check if it is equal to the value we are looking for.
3. If the value is found, return the index of that value.
4. If the end of the array is reached and the value is not found, return -1 to indicate that the value was not found.
'''

def LinearSearch(arr, targetVal):
    for i in range(len(arr)):
        if targetVal == arr[i]:
            return i
    return -1 

arr = [22, 55, 11, 0, 66, 33, 99]

targetVal = int(input("Enter the value you want to search: "))

result = LinearSearch(arr, targetVal)

if result != 1:
    print(f"Element found at position: ", result)
else:
    print("Not found")

