#A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.

n = int(input("Enter the number of elements you want to add in the stack: "))
stack = []
for i in range(n):
    element = input("Enter the element you want to add: ")
    stack.append(element) #push

TopElement = stack[-1] #peek
print("The Topmost element is:", TopElement) 

PoppedElement = stack.pop() #pop
print("The Popped element is: ", PoppedElement)
print("Current Stack: ", stack)

Size = len(stack) #size
print("Size of the stack: ", Size)