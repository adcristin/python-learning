'''
Graphs are non-linear because the data structure allows us to have different paths(edges) to get from one vertex to another, unlike with linear data structures like Arrays or Linked Lists.

A Graph representation tells us how a Graph is stored in memory.

Different Graph representations can:

1.take up more or less space.
2.be faster or slower to search or manipulate.
3.be better suited depending on what type of Graph we have (weighted, directed, etc.), and what we want to do with the Graph.
4.be easier to understand and implement than others.
'''

#Sample directed graph
n = 5
A = [[0, 1], [0, 3], [1, 2], [3, 4], [4, 2], [4, 5], [5, 2]]

#Adjacency Matrix Graph Representation
M = []

for i in range(n):
    M.append([0]*n)

for u, v in A:
    M[u][v] = 1

print(M)

#Adjacency List Graph Representation
from collections import defaultdict

D = defaultdict(list)

for u, v in A:
    D[u].append(v)

print(D)

#DFS - Recursive

def dfs_recursive(node):
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node)

source = 0 
seen = set()
seen.add(source)
dfs_recursive(source)

#DFS - Iterative

stack = [source]

while stack:
    node = stack.pop()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
           seen.add(nei_node)
           stack.append(nei_node)

#BFS

from collections import deque

q = deque()
q.append(source)

while q:
    node = q.popleft()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
           seen.add(nei_node)
           q.append(nei_node)

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def __str__(self):
        return f'Node({self.value})'
    
    def display(self):
        connections = [node.value for node in self.neighbors]
        return f'{self.value} is connected to: {connections}'
    
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

A.neighbors.append(B)
B.neighbors.append(A)

C.neighbors.append(D)
D.neighbors.append(C)