import networkx as nx
import pandas as pd

def Leerdatosdegrafo(file_path):
    G = nx.Graph()

    with open(file_path, 'r') as f:
        for line in f:
            node1, node2 = map(int, line.strip().split())
            G.add_edge(node1, node2)

    return G
def lecturapanda(file):
    data_network = pd.read_csv(
    file,
    header = None,
    sep = " ",
    names = ["user_1", "user_2"]
    )
    return data_network