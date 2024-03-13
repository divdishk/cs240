# Dijkstra's Algorithm

""" p-code
Dijkstra(graph, source):
    Initialize distances from source to all other vertices as infinity
    Set distance to source as 0
    Initialize priority queue Q
    Add source to Q
    while Q is not empty:
        u = vertex in Q with smallest distance
        Remove u from Q
        for each neighbor v of u:
            alt = distance[u] + weight(u, v)
            if alt < distance[v]:
                distance[v] = alt
                Add v to Q
    return distances
"""
import heapq

def Dijkstra(graph, source):  # function to find shortest paths using Dijkstra's algorithm
    distances = {vertex: float('infinity') for vertex in graph}
    # set distance of source vertex to 0
    distances[source] = 0
    priorityQueue = [(0, source)]

    while priorityQueue:
        # pop vertex with smallest distance from priority queue
        currentDistance, currentVertex = heapq.heappop(priorityQueue)

        # if the calculated distance is greater than the recorded, skip the iteration
        if currentDistance > distances[currentVertex]:
            continue
        # iterate over neighbors of current vertex
        for neighbor, weight in graph[currentVertex].items():
            distance = currentDistance + weight

            if distance < distances[neighbor]: # if distance is less than recorded, update distance
                distances[neighbor] = distance
                heapq.heappush(priorityQueue, (distance, neighbor))
    return distances

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 5, 'D': 10},
    'C': {'D': 3},
    'D':{}
}

source = 'A' # source vertex for calculating shortest paths
print(Dijkstra(graph,source)) # print