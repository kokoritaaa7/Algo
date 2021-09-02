graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F'],
    'D': ['A', 'G', 'H'],
    'E': ['B', 'I', 'J'],
    'F': ['C'],
    'G': ['D'],
    'H': ['D', 'K'],
    'I': ['E',],
    'J': ['E'],
    'K': ['H']
}

def dfs(graph, start_node):
    visited = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited

print(dfs(graph, 'A'))


def bfs(graph, start_node):
    visited = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited

print(bfs(graph,'A'))