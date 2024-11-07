import networkx as nx
import ast
# Función para leer el grafo desde un archivo con datos de texto (palabras separadas por espacios)
def Leerdatosdegrafo_texto(file_path):
    transacciones = []  # Lista para almacenar las transacciones

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()  # Eliminamos los espacios al principio y al final de la línea
            if line:  # Si la línea no está vacía
                # Convertimos la cadena de la línea a una lista utilizando ast.literal_eval
                transaccion = ast.literal_eval(line)
                transacciones.append(transaccion)

    return transacciones


# Función para leer el grafo desde un archivo con datos numéricos (separados por espacios)
def Leerdatosdegrafo_numeros(file_path):
    G = nx.Graph()  # Creamos un grafo no dirigido

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()  # Eliminamos los espacios en blanco al inicio y al final
            if line:  # Si la línea no está vacía
                node1, node2 = map(int, line.split())  # Convertimos los nodos en enteros y los agregamos como aristas
                G.add_edge(node1, node2)

    return G