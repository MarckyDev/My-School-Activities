# DEPTH FIRST SEARCH

def DFS(graph, root):
    visited, stack = set(), [root]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
    return visited


tree = {1: [2, 4, 5],
        2: [1, 3],
        3: [2],
        4: [1],
        5: [1, 6],
        6: [7, 8],
        7: [6],
        8: [6]}

print(DFS(tree, 5))
