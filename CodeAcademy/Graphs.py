def dfs(graph, current_vertex, target_value, visited=None):
    if visited is None:
        visited = []
	
    visited.append(current_vertex)
    if current_vertex == target_value:
        return visited
	
    # Add your recursive case here:
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, target_value, visited)
            if path:
                return path


the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
}

# Call dfs() below and print the result:
print(dfs( the_most_dangerous_graph, "crocodiles" , "bees"))


the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
}

def bfs(graph, start_vertex, target_value):
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    bfs_queue = [vertex_and_path]
    visited = set()
    
    while bfs_queue:
        current_vertex, path = bfs_queue.pop(0)
        visited.add(current_vertex)
        
        for neighbor in graph[current_vertex]:
        # Finish the function here:
            if neighbor not in visited:
                if neighbor == target_value:
                    return path + [neighbor]
                else:
                    bfs_queue.append([neighbor, path + [neighbor]])

# Call bfs() below and print the result:
print(bfs( the_most_dangerous_graph, "crocodiles", "bees"))


# Which for loop might be part of a breadth-first search Python implementation?
for neighbor in graph[current_vertex]:
    if neighbor not in visited:
        if neighbor is target_value:
            return path + [neighbor]
    else:
        search_queue.append([neighbor, path + [neighbor]])

# Complete the if statement in this depth-first search implementation.

def dfs(graph, current_vertex, target_value, visited = None):
    if #What goes here? <---- :
        visited = []
    visited.append(current_vertex)
    if current_vertex is target_value:
        return visited
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            return dfs(graph, neighbor, target_value, visited)

some_important_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
}

# visited is None

# In a DFS implementation looking for a path between two points, what happens if the current vertex has the target value?
if current_vertex is target_value:
    return visited


# Complete the if statement in this depth-first search implementation.

def dfs(graph, current_vertex, target_value, visited = None):
    if #What goes here? <---- :
    visited = []
    visited.append(current_vertex)
    if current_vertex is target_value:
        return visited
    
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
        return dfs(graph, neighbor, target_value, visited)
      
some_important_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
}

# visited is None
# If visited is None, then this is not a recursive call of the function and visited needs to be given the value of an empty list.


# What’s the purpose of having a set called visited in a BFS Python implementation?
# To store up all visited vertices so as not to revist any

# Quiz: Graph Search: Python
# Which for loop might be part of a breadth-first search Python implementation?

# A:
for neighbor in graph[current_vertex]:
    if neighbor not in visited:
        if neighbor is target_value:
            return path + [neighbor]
        else:
        search_queue.append([neighbor, path + [neighbor]])
        
    # B:
for neighbor in graph[current_vertex]:
    if neighbor not in visited:
        return search(graph, neighbor, target_value, visited)
    
# This would be a DFS for loop which includes a recursive return statement for unvisited vertices. BFS implemetations employ a search queue to find unvisited vertices

# Answer is A


# Quiz: Graph Search: Python
# Complete the return statement for the base case of this DFS implementation:

def dfs(graph, current_vertex, target_value, visited = None):
    if visited is None:
        visited = []
    visited.append(current_vertex)
    if current_vertex is target_value:
        return # What goes here?
    
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            return dfs(graph, neighbor, target_value, visited)
# visited
        

# Why is visited included in the parameters of this depth-first search implementation?

def dfs(graph, current_vertex, target_value, visited = None):
    if visited is None:
        visited = []
        
    visited.append(current_vertex)
    
    if current_vertex is target_value:
        return visited
    
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            return dfs(graph, neighbor, target_value, visited)
        
# visited will be passed in to continue building out the path during recursive calls

# Inside a breadth-first search implementation, you have a for loop of the current vertex’s neighboring vertices. What needs to be true in this loop in order for the path to be returned?

# the neighboring vertex has been visited AND the neighboring vertex has the target value



# What is wrong with the following pseudocode for Dijkstra’s algorithm?

# - Set all distances to all other vertices from start vertex to infinity
# - while heap exists:
#     - pop vertex with mininum distance
#     - check neighbors of that vertex:
#           - new distance = distance to vertex + edge weight
#           - if new distance > current distance:
#                  - replace current distance with new distance
# - return distances

# you should be checking if the new distance is less than the current distance
