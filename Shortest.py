from Read_Data import Leerdatosdegrafo #Con este modulo leemos la data
from BFS import bfs_paths #con este modulo utilizamos bfs
from DFS import dfs_paths #con este modulo utilizamos dfs
import timeit #para medir y comparar los tiempos

file = 'facebook_combined.txt' #la data
graph = Leerdatosdegrafo(file) #Establezco un el grafo en esta variable

start_node = 0 #Aqui ponemos el nodo con inicial 'start_node'
target_node = 2879 #nuestra función intentará buscar el camino más corto desde el start_node hasta este nodo (si es que existe)

##BFS
def BFS_search():
    paths_from_start = bfs_paths(graph, start_node) #aqui creamos un diccionario donde cada clave es un nodo que start_node puede alcanzar. cada valor es una lista que representa el camino más corto desde nuestro 'start mode'
    return paths_from_start.get(target_node, None)#aqui intentamos extraer el camino especifico entre startnode y target node. busca la clave targetnode dentro de pathsfromstart si target_node está en el diccionario denuelve el camino almacenado para ese nodo (que es el mas corto) si no hay camino, sale none
##DFS
def DFS_search():
    paths_from_start = dfs_paths(graph, start_node) # aqui creamos un diccionario desde el nodo de inicio hasta todos los demas nodos del grafo

    return paths_from_start.get(target_node, None) #aqui extraemos la clave que contiene el nodo target del diccionario

shortest_path_result = BFS_search()
deep_path_result = DFS_search()

# Muestra de resultados #
if shortest_path_result:
    print(f"Camino más corto entre {start_node} y {target_node}: {shortest_path_result}")
else:
    print(f"No hay camino disponible entre {start_node} y {target_node}")

if deep_path_result:
    print(f"Camino en profundidad entre {start_node} y {target_node}: {deep_path_result}")
else:
    print(f"No hay camino disponible entre {start_node} y {target_node}")

# Tiempos de ejecución #
execution_time = timeit.timeit("BFS_search()", globals=globals(), number=1)
print(f"Tiempo de ejecución ( BFS ): {execution_time:.5f} segundos")
execution_time = timeit.timeit("DFS_search()", globals=globals(), number=1)
print(f"Tiempo de ejecución ( DFS ): {execution_time:.5f} segundos")