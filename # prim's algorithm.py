# prim's algorithm

""" p-code 
Prim(graph, source):
    Initialize an empty set MST
    Initialize a priority queue Q
    Add source to Q with key 0
    while Q is not empty:
        u = vertex in Q with smallest key
        Remove u from Q
        Add u to MST
        for each neighbor v of u:
            if v is in Q and weight(u, v) < key[v]:
                update key[v] to weight(u, v)
                update parent[v] to u
    return MST
"""
import heapq
def prim(graph, source): # function to find MST using prim's algorithm
    # initializing an empty set to store vertices in the MST
    mst = set()
    priorityQueue = [(0, source)]
    keys = {vertex: float('infinity') for vertex in graph}
    parent = {vertex: None for vertex in graph}
    keys[source] = 0

    while priorityQueue:
        # pop vertex with minimum key from priority queue
        currentWeight, currentVertex = heapq.heappop(priorityQueue)

        # if vertex is already in MST, countine to next iteration
        if currentVertex in mst:
            continue
        mst.add(currentVertex) # add current vertex to MST

        # iterate over neighbors of current vertex
        for neighbor, weight in graph[currentVertex].items():
            if neighbor not in mst and weight < keys[neighbor]:
                keys[neighbor] = weight
                parent[neighbor] = currentVertex
                heapq.heappush(priorityQueue, (weight, neighbor))

    return parent 

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}

source = 'A' # source vertex for MST construction
print(prim(graph, source)) # print the parent dictionary representing the MST