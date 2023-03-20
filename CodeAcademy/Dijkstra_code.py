graph = {
    'A': [('B', 10), ('C', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 2)],
    'D': [('E', 10)],
    'E': [('B', 15)],
}


for vertex in graph:
    print("\n\nVertex {0} connects to: ".format(vertex))
    for edge in graph[vertex]:
        print("vertex {0} with a weight of {1}".format(edge[0], edge[1]))


import heapq


heap = [(0, 'A')]
heapq.heappush(heap, (1, 'B'))
heapq.heappush(heap, (-5, 'D'))
heapq.heappush(heap, (4, 'E'))
heapq.heappush(heap, (2, 'C'))

print("The smallest values in the heap in ascending order are:\n")
while heap:
    *print(heapq.heappop(heap))



from heapq import heappop, heappush
from math import inf

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [('A', 7)],
        'B': [('C', 3), ('D', 2)]
    }


def dijkstras(graph, start):
    distances = {}
    
    for vertex in graph:
        distances[vertex] = inf
        
    distances[start] = 0
    vertices_to_explore = [(0, start)]
    
    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore)
        
        for neighbor, edge_weight in graph[current_vertex]:
        new_distance = current_distance + edge_weight
        
        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            heappush(vertices_to_explore, (new_distance, neighbor))
            
    return distances
            
distances_from_d = dijkstras(graph, 'D')
print("\n\nShortest Distances: {0}".format(distances_from_d))