def dfs_paths(graph, start):
    stack = [(start, [start])]  # Pila que contiene el nodo y el camino hasta él
    visited = set([start])
    paths = {start: [start]}  # Diccionario que guarda el camino a cada nodo

    while stack:
        current_node, path = stack.pop()

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                paths[neighbor] = new_path  # Guardamos el camino al vecino
                stack.append((neighbor, new_path))

    return paths
