#dfs
from collections import deque

def dfs(node, targetValue):
    searchStack = [node]# Initialize the stack with the starting node
    searched = set() # Track visited nodes
    while searchStack:
        currentNode = searchStack.pop()# Pop the last node from the stack
        if currentNode not in searched:
            print(currentNode)
            if currentNode == targetValue:
                return True
            else:
                searchStack.extend(graph[currentNode])# Add neighbors to the stack
                searched.add(currentNode)# Mark the current node as visited
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

print(dfs('A', 'G'))  