from collections import deque

def bfs_paths(graph, start):
    queue = deque([(start, [start])])  # La cola ahora incluye el camino hasta el nodo actual
    visited = set([start])
    paths = {start: [start]}  # Diccionario que almacena el camino más corto a cada nodo

    while queue:
        current_node, path = queue.popleft()

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                paths[neighbor] = new_path  # Guardamos el camino a cada nodo alcanzable
                queue.append((neighbor, new_path))

    return paths
