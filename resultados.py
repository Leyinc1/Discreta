import networkx as nx
import pandas as pd
import warnings
##import matplotlib.pyplot as plt
import funcionesGrafos as fg
from Read_Data import lecturapanda
warnings.filterwarnings("ignore")

#Lectura de datos
data_network = lecturapanda("Datos.txt")

#print(data_network)

#Creación de grafo
graph_network = nx.from_pandas_edgelist(data_network, 
                                        source = "user_1", 
                                        target = "user_2",
                                        create_using = nx.Graph())

#print(graph_network)
#Problema 1
nroGrupAmigos = fg.find_friend_groups_dfs(graph_network)
print("El número de grupos de amigos distintos es ", nroGrupAmigos)

#Problema 2
listaRecomendaciones = fg.recommend_friends(graph_network)
print("Listas de recomendaciones de amistad para cada persona:\n", listaRecomendaciones)

#Problema 3
resPopFriend = fg.most_popular_friend(graph_network)
if resPopFriend[1] > 0:
    print("El amigo más popular es: ", resPopFriend[0])
    print("Su número de amigos es: ", resPopFriend[1])
else:
    print("No existe un amigo popular.\n")