import networkx as nx
from networkx import shortest_path, shortest_path_length
import random
import matplotlib.pyplot as plt
from itertools import combinations, groupby
import os
import json

def load_graph_from_json(path):
    f = open(path)

    data = json.load(f)
    f.close()

    node_set = data['nodes']
    source_node = min(node_set)
    target_node = max(node_set)
    edge_set = data['edges']
    #print(edge_set)
    distances_set = data['distance']

    G = nx.Graph()
    G.add_nodes_from(node_set)
    for i in range(len(distances_set)):
        G.add_edge(edge_set[i][0], edge_set[i][1], distance=distances_set[i])

    return G, source_node, target_node, distances_set, node_set

print (os.path.abspath('.'))
G,  source_node, target_node, distances_set, node_set = load_graph_from_json('/Users/yujunchi/Documents/GitHub/tree-of-thought-llm/data/shortest_path/easy-5shot/4.json')

path = shortest_path(G, source=source_node, target=target_node, weight='distance')
length = shortest_path_length(G, source=source_node, target=target_node, weight='distance')
print('Node set:', node_set)
print('Edge set:', G.edges)
print('Edge distance set:', distances_set)
print(path, length)







