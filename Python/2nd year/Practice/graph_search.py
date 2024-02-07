def shortest_path(graph, starting_point, end_point = None):
    visited_nodes = []
    queue = [starting_point]
    distance = {starting_point: 0}

    while queue:
        current_node = queue.pop(0)
        if current_node not in visited_nodes:
            visited_nodes.append(current_node)
            if current_node == end_point:
                break
        
        for neighbor in graph[current_node]:
            if neighbor not in visited_nodes:
                queue.append(neighbor)
                distance[neighbor] = distance[current_node] + 1
    
    path = [end_point]

    while path[-1] != starting_point:
        for neighbor in graph[path[-1]]:
            if neighbor in distance and distance[neighbor] == distance[path[-1]] - 1:
                path.append(neighbor)
                break

    
    return path
    


maze = {
    1: [2, 5],
    2: [1, 3, 4],
    3: [2, 4],
    4: [2, 3, 5],
    5: [1, 4]}

print(shortest_path(maze, 2, 5))

# ---------------------------------------------------------------------------- #
#                                     MAZE                                     #
# ---------------------------------------------------------------------------- #
#######################################################
# 1 ------> 2
# |         |
# |         |
# |         v
# |         3 -----> 4
# |                 /
# |                /
# |               /
# |              /
# |             /
# |            /
# |           /
# |          /
# |         /
# |        /
# |       /
# |      /
# |     /
# |    /
# |   /
# |  /
# v /
# 5
######################################################
