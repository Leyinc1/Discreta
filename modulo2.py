import itertools
from collections import defaultdict


# Función para construir el grafo de co-ocurrencia
def construir_grafo_coocurrencia(transacciones, k):
    # Diccionario para contar cuántas veces aparecen juntos dos artículos
    conteo_pares = defaultdict(int)

    # Iterar sobre todas las transacciones
    for transaccion in transacciones:
        # Crear todas las combinaciones posibles de pares de artículos en la transacción
        for articulo1, articulo2 in itertools.combinations(transaccion, 2):
            # Ordenar los artículos para evitar duplicados (A-B es igual a B-A)
            articulo1, articulo2 = sorted([articulo1, articulo2])
            conteo_pares[(articulo1, articulo2)] += 1

    # Crear el grafo de co-ocurrencia
    grafo_coocurrencia = defaultdict(list)

    # Añadir una arista entre los nodos si el conteo de pares es mayor o igual a k
    for (articulo1, articulo2), conteo in conteo_pares.items():
        if conteo >= k:
            grafo_coocurrencia[articulo1].append(articulo2)
            grafo_coocurrencia[articulo2].append(articulo1)

    return grafo_coocurrencia


# Función para mostrar el grafo de co-ocurrencia
def mostrar_grafo_coocurrencia(grafo):
    for articulo, vecinos in grafo.items():
        print(f"{articulo} está conectado con: {', '.join(vecinos)}")



