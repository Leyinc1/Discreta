from Read_Data import Leerdatosdegrafo
import timeit

file_path = 'facebook_combined.txt'
graph = Leerdatosdegrafo(file_path)

def find_cycle(graph):
    visited = set() #creé este conjunto para evitar a registrar nodos ya revisados
    cycle_path = [] #aqui vamos a introducir los ciclos que se encuentren

    def detect_cycle(node, path): #recursiva, explora cada vecino de el nodo actual. si su vecino ya está en PATH, significa que se ha formado un ciclo.
        for neighbor in graph.neighbors(node):
            if neighbor in path:  # Si el vecino está en el camino actual, hay un ciclo
                # Construimos el ciclo
                cycle_path.extend(path[path.index(neighbor):] + [neighbor])
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                if detect_cycle(neighbor, path + [neighbor]):
                    return True
        return False

    for node in graph.nodes():
        if node not in visited:
            visited.add(node)
            if detect_cycle(node, [node]):
                return cycle_path

    return None

# Ejecución de la función para detectar ciclos
cycle = find_cycle(graph)
if cycle:
    print(f"Se encontró un ciclo: {cycle}")
else:
    print("No se encontró ningún ciclo.")

execution_time = timeit.timeit("find_cycle(graph)", globals=globals(), number=1)
print(f"Tiempo de ejecución ( find_cycle ): {execution_time:.5f} segundos")