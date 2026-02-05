'''
A Binary Tree is a type of tree data structure where each node can have a maximum of two child nodes, a left child node and a right child node.

This restriction, that a node can have a maximum of two child nodes, gives us many benefits:

Algorithms like traversing, searching, insertion and deletion become easier to understand, to implement, and run faster.
Keeping data sorted in a Binary Search Tree (BST) makes searching very efficient.
Balancing trees is easier to do with a limited number of child nodes, using an AVL Binary Tree for example.
Binary Trees can be represented as arrays, making the tree more memory efficient.
'''

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = BinaryTree(0)
node1 = BinaryTree(1)
node2 = BinaryTree(2)
node3 = BinaryTree(3)
node4 = BinaryTree(4)
node5 = BinaryTree(5)
node6 = BinaryTree(6)
node7 = BinaryTree(7)

root.left = node1
root.right = node2

node1.left = node3
node1.right = node4

node2.left = node5
node2.right = node6

node6.left = node7

print("root.right.right.left.data:", root.right.right.left.data)

'''
Binary tree traversal:

Breadth First Search (BFS) is when the nodes on the same level are visited before going to the next level in the tree. This means that the tree is explored in a more sideways direction.

Depth First Search (DFS) is when the traversal moves down the tree all the way to the leaf nodes, exploring the tree branch by branch in a downwards direction.

There are three different types of DFS traversals:

1.pre-order
2.in-order
3.post-order
'''

#pre-order
def PreOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    PreOrderTraversal(node.left)
    PreOrderTraversal(node.right)

#in-order
def InOrderTraversal(node):
    if node is None:
        return
    InOrderTraversal(node.left)
    print(node.data, end=", ")
    InOrderTraversal(node.right)

#post-order
def PostOrderTraversal(node):
    if node is None:
        return
    PostOrderTraversal(node.left)
    PostOrderTraversal(node.right)
    print(node.data, end=", ")

PreOrderTraversal(root)
print()
InOrderTraversal(root)
print()
PostOrderTraversal(root)
