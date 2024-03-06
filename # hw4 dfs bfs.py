# hw4 dfs bfs
from collections import deque

def dfsIterative(graph, start, end):
    # intializes a stack to keep track of nodes that need to be visited
    stack = [start]
    # intializes a set to keep track of already visited nodes
    visited = set()
    while stack:
        node = stack.pop() # pops the last node from the stack
        # if node reaches its end point, return true
        if node == end:
            return True
        if node not in visited:
            # mark node as visited
            visited.add(node)
            # extend the stack with the neighbors of the current node
            stack.extend(graph[node])
            # if destination not found, return false
    return False

def bfsShortestPath(graph, start, end):
    # intialize a deque for BFS transversal
    queue = deque([(start, [start])])
    while queue:
        # dequeue the first node and its path from the queue
        node, path = queue.popleft()
        # if node reaches end point return path
        if node == end:
            return path
        # iterate over the neighbirs of the current node
        for neighbor in graph[node]:
            if neighbor not in path:
                # enques the neighor and the path to the quque
                queue.append((neighbor, path + [neighbor]))
    # if theres no path, return None
    return None

# Example usage
graph = {
    'Room A': ['Room B', 'Room C'],
    'Room B': ['Room D'],
    'Room C': ['Room E'],
    'Room D': ['Room F'],
    'Room E': ['Room F'],
    'Room F': []
}
startRoom = 'Room A'
endRoom = 'Room F'

print("DFS Path exists (Iterative):", dfsIterative(graph, startRoom, endRoom))  # Output: True
print("BFS Shortest Path (Iterative):", bfsShortestPath(graph, startRoom, endRoom))  # Output: ['Room A', 'Room C', 'Room E', 'Room F']
