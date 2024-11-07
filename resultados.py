import timeit
import time
import networkx as nx
from Read_Data import Leerdatosdegrafo_texto, Leerdatosdegrafo_numeros
from Read_Data import Leerdatosdegrafo_numeros
import funcionesGrafos as fg
import modulo1 as m1
import modulo2 as m2
import modulo3 as m3
# Cargar datos
file = 'Datos.txt'  # Reemplaza con tu archivo de datos
graph_network = Leerdatosdegrafo_numeros(file)

#Social Networks
# Mostrar número de grupos de amigos (con DFS y BFS)
nroGruposDFS = fg.find_friend_groups_dfs(graph_network)
nroGruposBFS = fg.find_friend_groups_bfs(graph_network)
print(f"Número de grupos de amigos (DFS): {nroGruposDFS}")
print(f"Número de grupos de amigos (BFS): {nroGruposBFS}")

# Mostrar recomendaciones de amistad
recomendaciones = fg.recommend_friends(graph_network)
print("Recomendaciones de amistad:", recomendaciones)

# Mostrar el amigo más popular
amigoPopular, nroAmigos = fg.most_popular_friend(graph_network)
print(f"Amigo más popular: {amigoPopular} con {nroAmigos} amigos.")

# Tiempo de ejecución para encontrar grupos de amigos usando DFS y BFS
execution_time_dfs = timeit.timeit(lambda: fg.find_friend_groups_dfs(graph_network), number=1)
execution_time_bfs = timeit.timeit(lambda: fg.find_friend_groups_bfs(graph_network), number=1)
print(f"Tiempo de ejecución (DFS): {execution_time_dfs:.5f} segundos")
print(f"Tiempo de ejecución (BFS): {execution_time_bfs:.5f} segundos")

# Verificar si hay ciclos en el grafo
cycle_exists = fg.has_cycle(graph_network)
print("¿El grafo tiene ciclos?", "Sí" if cycle_exists else "No")

# Ejemplo de uso de shortest_path
person1 = 1  # Reemplaza con el nodo inicial
person2 = 2  # Reemplaza con el nodo objetivo
path = fg.shortest_path(graph_network, person1, person2)
if path:
    print(f"El camino más corto entre {person1} y {person2} es: {path}")
else:
    print(f"No hay camino entre {person1} y {person2}.")
print("========================================================================")
#Market Basket Analysis
#Pregunta 1
file = 'DatosL.txt'  # Ruta al archivo de transacciones
transacciones = Leerdatosdegrafo_texto(file)  # Leemos las transacciones desde el archivo

soporte_minimo = 2
conjuntos_frecuentes = m1.crecimiento_fp(transacciones, soporte_minimo)
print("Conjuntos frecuentes:", conjuntos_frecuentes)
# tiene una complejidad cuaratica ya que el peor de los casos en el que cada row contenga todos los productos tiene que comprobar el numero de productos por el numero de productos n*n, ademas de que eto se multiplica por el numero de rows al final

print("=======================================================================")
#Pregunta 2
k = 2
grafo = m2.construir_grafo_coocurrencia(transacciones, k)
m2.mostrar_grafo_coocurrencia(grafo)
print("=======================================================================")
#un grafo indica la relacion entre dos nodos los cuales pueden tener multiples conexiones con otros, y a su vez llevar un counting para verificar la recurrencia de la misma.
#Pregunta 3
k = 2
grafo = m3.construir_grafo_coocurrencia(transacciones, k)

# Medir tiempo de ejecución para DFS
inicio_dfs = time.time()
comunidades_dfs = m3.encontrar_comunidades_dfs(grafo)
fin_dfs = time.time()
tiempo_dfs = fin_dfs - inicio_dfs

# Medir tiempo de ejecución para BFS
inicio_bfs = time.time()
comunidades_bfs = m3.encontrar_comunidades_bfs(grafo)
fin_bfs = time.time()
tiempo_bfs = fin_bfs - inicio_bfs

# Mostrar los resultados
print("Comunidades encontradas con DFS:")
for idx, comunidad in enumerate(comunidades_dfs):
    print(f"Comunidad {idx + 1}: {', '.join(comunidad)}")
print(f"Tiempo de ejecución con DFS: {tiempo_dfs} segundos\n")

print("Comunidades encontradas con BFS:")
for idx, comunidad in enumerate(comunidades_bfs):
    print(f"Comunidad {idx + 1}: {', '.join(comunidad)}")
print(f"Tiempo de ejecución con BFS: {tiempo_bfs} segundos")

#las comunidades son identificadas debido a la recurrencia entre las relaciones entre nodos, esta recurrencia indica un peso, si este patron de relacion se cumplen n veces, suma n al peso. De esta manera identificamos el patron de compra, por la frecuencia entre las relaciones.
