from collections import defaultdict, deque
import itertools


# Función para realizar la búsqueda en profundidad (DFS) y encontrar una comunidad
def dfs(grafo, nodo, visitado, comunidad):
    visitado.add(nodo)  # Marcar el nodo como visitado
    comunidad.append(nodo)  # Añadir el nodo a la comunidad actual

    # Recorrer los vecinos del nodo
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs(grafo, vecino, visitado, comunidad)

# Función para encontrar todas las comunidades usando DFS
def encontrar_comunidades_dfs(grafo):
    visitado = set()  # Para llevar el registro de los nodos visitados
    comunidades = []  # Lista para almacenar todas las comunidades

    # Iterar sobre todos los nodos del grafo
    for nodo in grafo:
        if nodo not in visitado:
            comunidad = []
            dfs(grafo, nodo, visitado, comunidad)
            comunidades.append(comunidad)

    return comunidades

# Función para realizar la búsqueda en anchura (BFS) y encontrar una comunidad
def bfs(grafo, nodo, visitado, comunidad):
    cola = deque([nodo])
    visitado.add(nodo)

    while cola:
        actual = cola.popleft()
        comunidad.append(actual)

        for vecino in grafo[actual]:
            if vecino not in visitado:
                visitado.add(vecino)
                cola.append(vecino)

# Función para encontrar todas las comunidades usando BFS
def encontrar_comunidades_bfs(grafo):
    visitado = set()
    comunidades = []

    for nodo in grafo:
        if nodo not in visitado:
            comunidad = []
            bfs(grafo, nodo, visitado, comunidad)
            comunidades.append(comunidad)

    return comunidades

# Función para construir el grafo de co-ocurrencia
def construir_grafo_coocurrencia(transacciones, k):
    conteo_pares = defaultdict(int)

    # Contar la co-ocurrencia de artículos en las transacciones
    for transaccion in transacciones:
        for articulo1, articulo2 in itertools.combinations(transaccion, 2):
            articulo1, articulo2 = sorted([articulo1, articulo2])
            conteo_pares[(articulo1, articulo2)] += 1

    # Crear el grafo de co-ocurrencia
    grafo_coocurrencia = defaultdict(list)
    for (articulo1, articulo2), conteo in conteo_pares.items():
        if conteo >= k:
            grafo_coocurrencia[articulo1].append(articulo2)
            grafo_coocurrencia[articulo2].append(articulo1)

    return grafo_coocurrencia


