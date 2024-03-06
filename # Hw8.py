# Hw8
# BFS is ideal for searching trees and graphs when you want to visit the 
# neighbors of the node before moving on to the next set of neighbors.
# Time complexity: O(V+E), every vertex is visited at least once O(V),  and every edge ]
# is visited once as bfs explores the edges incident to each vertex O(E).

from collections import deque
import graphlib

def bfs(node, targetValue):
    searchQueue = deque()# Create a double-ended queue
    searchQueue.extend(graph[node])# Add neighbors of the starting node to the queue
    searched = set()  # Track visited nodes
    while searchQueue:
        currentNode = searchQueue.popleft()# Retrieve and remove the first node from the queue
        if currentNode not in searched:
            print(currentNode)
            if currentNode == targetValue:
                return True
            else:
                searchQueue.extend(graph[currentNode])# Add neighbors of the current node to the queue
                searched.add(currentNode)                 # Mark the current node as visited
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

print(bfs('A', 'G'))
