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
    print(heapq.heappop(heap))