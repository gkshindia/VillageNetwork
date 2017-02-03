# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 14:12:42 2017

@author: KANHAIYA
"""

import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import numpy as np
'''G = nx.karate_club_graph()
nx.draw(G, with_labels = True, node_color = "blue", edge_color = "gray")'''

N = 20
p = 0.4 #probability of connection between the nodes above
def er_graph(N, p):
    ''' Generates a ER graph'''
    G = nx.Graph()
    G.add_nodes_from([range(N)])
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p = p):
                G.add_edge(node1,node2)
    return G
nx.draw(er_graph(50,0.08), node_size = 40, node_color = "light blue")

def plot_deg_distribution(G):
    plt.hist(list(G.degree().values()), histtype = "step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")
    
A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter = ",")
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter = ",")
G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

def basic_net_stats(G):
    print("Number of nodes: %d" % G.number_of_nodes())
    print("Number of edges: %d" % G.number_of_edges())
    print("Mean of Edges:- %.2f" % np.mean(list(G.degree().values())))
    
plot_deg_distribution(G1)
plot_deg_distribution(G2)
plt.savefig("Villagehist.pdf")

gen = nx.connected_component_subgraphs(G1)
g = gen.__next__()
g.number_of_nodes()

G1_LCC = max(nx.connected_component_subgraphs(G1), key = len)
G2_LCC = max(nx.connected_component_subgraphs(G2), key = len)
plt.figure()
nx.draw(G1_LCC, node_color = 'red', edge_color = 'gray', node_size = 20)
plt.savefig("Village1.pdf")
nx.draw(G2_LCC, node_color = 'blue', edge_color = 'pink', node_size = 20)
plt.savefig("Village2.pdf")