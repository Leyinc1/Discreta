import networkx as nx
import pandas as pd
from collections import deque 
import warnings
##import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

def dfs(persona, personVisit, graph):
    if personVisit[persona]: return
    personVisit[persona] = True
    
    for amigo in graph.neighbors(persona):
        dfs(amigo, personVisit, graph) 

def find_friend_groups_dfs(graph):
    nroGrupos = 0
    personVisit = {}
    
    for persona in graph.nodes():
        personVisit[persona] = False

    for persona in graph.nodes():
        if not personVisit[persona]:
            nroGrupos += 1
            dfs(persona, personVisit, graph)

    return nroGrupos
#complejidad temporal: O(V+E)
#complejidad espacial: O(V+E)

def bfs(personaIni, visit, graph):
    cola = deque([personaIni])
    visit.add(personaIni)
    
    while cola:
        actual = cola.popleft()
        for amigo in graph.neighbors(actual):
            if amigo not in visit:
                visit.add(amigo)
                cola.append(amigo)

def find_friend_groups_bfs(graph):
    nroGrupos = 0
    personVisit = {}
    
    for persona in graph.nodes():
        personVisit[persona] = False

    for persona in graph.nodes():
        if not personVisit[persona]:
            nroGrupos += 1
            bfs(persona, personVisit, graph)

    return nroGrupos

    
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

def most_popular_friend(graph):
    nroAmigos = 0
    for nodo in graph.nodes():
        if nroAmigos < graph.degree[nodo]:
            amigoPopular = nodo
            nroAmigos = graph.degree[nodo]
    return [amigoPopular, nroAmigos]

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
