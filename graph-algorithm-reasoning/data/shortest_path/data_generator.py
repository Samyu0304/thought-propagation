import networkx as nx
import random
import matplotlib.pyplot as plt
from itertools import combinations, groupby
import os
import json
from networkx import shortest_path, shortest_path_length, single_source_dijkstra, dijkstra_path

def gnp_random_connected_graph(n, p):
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted
    """
    edges = combinations(range(n), 2)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < p:
                G.add_edge(*e)
    return G

def save_graph(G, source_target_path,length, path): 
    # cvt G_graph into  dict()
    graph_dict = {}
    graph_dict['nodes']=list(G.nodes)

    edge_list = []
    dist_list = []
    for node1, node2, data in G.edges(data=True):
        edge_list.append((node1, node2))
        dist_list.append(data['dist'])
    
    graph_dict['edges'] = edge_list
    graph_dict['distance'] = dist_list

    graph_dict['shortest_path'] = source_target_path
    graph_dict['shortest_length'] = length

    b = json.dumps(graph_dict)
    f = open(path, 'w')
    f.write(b)
    f.close()

def get_path_length(path, distance, edges):
    path_num_idx = len(path)
    path_length = 0
    for i in range(0, path_num_idx-1):
        if path[i]<path[i+1]:
            pair = (path[i], path[i+1])
        else:
            pair = (path[i+1], path[i])
        pair_index = edges.index(pair)
        path_length += distance[pair_index]
    
    return path_length

    

# define the node in graph [5, 10, 100, 0.2] >=3, [11,20,100,0.1]>=5, [21,30,100,0.1]>=8
St = 5
Ed = 10
Gem_Num = 100
Edge_prob = 0.2
trivial = 2
data_dir = './data/shortest_path/hard-5shot'
if not os.path.isdir(data_dir):
    os.mkdir(data_dir)

for i in range(0,Gem_Num):
    path_node_num = 1
    print(i)

    Num_nodes = random.randint(St, Ed)

    while path_node_num <= trivial:
        G = gnp_random_connected_graph(Num_nodes, p=Edge_prob)

        for u, v in G.edges():
            edge_distance = random.randint(1, 5)
            G.add_edge(u, v, dist=edge_distance)
        
        edge_list = []
        dist_list = []
        for node1, node2, data in G.edges(data=True):
            edge_list.append((node1, node2))
            dist_list.append(data['dist'])

        # compute gt shortest_path and length, only used for eval, and we filter out the data with trivial solutions.
        source_node = min(G.nodes)
        target_node = max(G.nodes)
        source_target_path = shortest_path(G, source=source_node, target=target_node, weight='dist')
        #print(source_target_path, dist_list, edge_list)
        length = get_path_length(source_target_path, dist_list, edge_list)
        #print(length, source_target_path)
        
        path_node_num = len(source_target_path)

    path = str(i) + '.json'
    path = os.path.join(data_dir,path)
    save_graph(G,source_target_path,length,path)

    

    

