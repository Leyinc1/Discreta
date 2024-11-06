import networkx as nx

def Leerdatosdegrafo(file_path):
    G = nx.Graph()

    with open(file_path, 'r') as f:
        for line in f:
            node1, node2 = map(int, line.strip().split())
            G.add_edge(node1, node2)

    return G


