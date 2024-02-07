# BREADTH FIRST SEARCH ALGORITHM
# shortest between nodes 

def BFS(graph, starting_node):
    visited = []
    queue = [starting_node]
    
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            visited.append(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
           
    return visited


tree = {1: [2, 4, 5],
        2: [1, 3],
        3: [2],
        4: [1],
        5: [1, 6],
        6: [7, 8],
        7: [6],
        8: [6]}

print(BFS(tree, 1))
