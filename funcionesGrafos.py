import networkx as nx
from collections import deque

# DFS iterativo
def dfs(persona, personVisit, graph):
    stack = [persona]  # Usamos una pila explícita para evitar recursión
    while stack:
        actual = stack.pop()  # Tomamos el último nodo de la pila
        if not personVisit[actual]:
            personVisit[actual] = True
            for amigo in graph.neighbors(actual):
                if not personVisit[amigo]:
                    stack.append(amigo)

# Encontrar grupos de amigos usando DFS
def find_friend_groups_dfs(graph):
    nroGrupos = 0
    personVisit = {persona: False for persona in graph.nodes()}
    for persona in graph.nodes():
        if not personVisit[persona]:
            nroGrupos += 1
            dfs(persona, personVisit, graph)
    return nroGrupos

# BFS auxiliar
def bfs(personaIni, visit, graph):
    cola = deque([personaIni])
    visit.add(personaIni)  # Usamos 'add' en un set, no en un diccionario
    while cola:
        actual = cola.popleft()
        for amigo in graph.neighbors(actual):
            if amigo not in visit:
                visit.add(amigo)
                cola.append(amigo)


# Encontrar grupos de amigos usando BFS
def find_friend_groups_bfs(graph):
    nroGrupos = 0
    personVisit = set()  # Usamos un set vacío en lugar de un diccionario
    for persona in graph.nodes():
        if persona not in personVisit:  # Reemplazamos la lógica de diccionario por set
            nroGrupos += 1
            bfs(persona, personVisit, graph)
    return nroGrupos

# Recomendación de amigos
def recommend_friends(graph):
    recomendaciones = {}
    for persona in graph.nodes():
        amigosDirect = set(graph.neighbors(persona))
        amigosRecomend = set()
        for amigo in amigosDirect:
            amigosDeAmigo = set(graph.neighbors(amigo))
            amigosRecomend.update(amigosDeAmigo - amigosDirect - {persona})
        recomendaciones[persona] = list(amigosRecomend)
    return recomendaciones

# Encontrar el amigo más popular
def most_popular_friend(graph):
    amigoPopular = max(graph.nodes, key=lambda x: graph.degree[x])
    nroAmigos = graph.degree[amigoPopular]
    return amigoPopular, nroAmigos

# Camino más corto usando BFS
def bfs_paths(graph, start):
    queue = deque([(start, [start])])
    visited = set([start])
    paths = {start: [start]}
    while queue:
        current_node, path = queue.popleft()
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                paths[neighbor] = new_path
                queue.append((neighbor, new_path))
    return paths

# Camino más corto usando DFS
def dfs_paths(graph, start):
    stack = [(start, [start])]
    visited = set([start])
    paths = {start: [start]}
    while stack:
        current_node, path = stack.pop()
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                paths[neighbor] = new_path
                stack.append((neighbor, new_path))
    return paths

# Verificar si hay ciclos en el grafo
def has_cycle(graph):
    visited = set()

    def dfs_cycle(node, parent):
        visited.add(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                if dfs_cycle(neighbor, node):
                    return True
            elif parent != neighbor:
                return True
        return False

    return any(dfs_cycle(node, None) for node in graph if node not in visited)
def shortest_path(graph, person1, person2):
    # Usar BFS para encontrar el camino más corto entre person1 y person2
    if person1 == person2:
        return [person1]

    # Cola para BFS, con el nodo inicial y el camino
    queue = deque([(person1, [person1])])
    visited = set([person1])

    while queue:
        current_node, path = queue.popleft()

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                if neighbor == person2:
                    return path + [neighbor]
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # Si no hay un camino entre person1 y person2
