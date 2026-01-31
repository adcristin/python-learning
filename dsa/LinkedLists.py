#A Linked List is, as the word implies, a list where the nodes are linked together. Each node contains data and a pointer. The way they are linked together is that each node points to where in the memory the next node is placed.

class SinglyLinkedList():
    
    def __init__(node, value):
        node.value = value
        node.next = None
    
def TraversingLinkedList(head): #Traversing
    curr = head
    while curr:
        print(curr.value, end=" -> ")
        curr = curr.next
    print("Null")


head = SinglyLinkedList(1)
node2 = SinglyLinkedList(2)
node3 = SinglyLinkedList(3)

head.next = node2
node2.next = node3

TraversingLinkedList(head)

        