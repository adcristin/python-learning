#A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.

n = int(input("Enter the number of elements you want to add in the queue: "))
queue = []
for i in range(n):
    element = input("Enter the element you want to add: ")
    queue.append(element) #enqueue

FrontElement = queue[0] #peek
RearElement = queue[-1]
print("The First element is:", FrontElement) 
print("The Last element is:", RearElement) 

DequeuedElement = queue.pop() #dequeue
print("The Popped element is: ", DequeuedElement)
print("Current queue: ", queue)

Size = len(queue) #size
print("Size of the queue: ", Size)