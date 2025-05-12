from pylab import *
import networkx as nx
import random
from plot_helper import plot_average_degrees
import numpy as np

m0= 100 # numero de nodos al inicio de la red 
m = 4 # numero de enlaces para cada nuevo nodo
p_e = 0.5
edge_avg = []

def initialize():
    global g
    g = nx.barabasi_albert_graph(m0, m, seed=None)
    g.pos = nx.spring_layout(g)
    g.count = 0 

def observe():
    global g
    cla()
    nx.draw(g, pos = g.pos, cmap= cm.bwr, vmin=0, vmax=1)

def update():
    global g
    g.count +=1

    # `p_e` can be understood as the probability of adding an edge between the new node and a random node in the graph
    nds = list(g.nodes)
    new_comer = max(nds) + 1 # designation of the new node

    for i in range(m):
        # Selection of a random node from the graph
        j = pref_select(nds)

        # Adds a new edge between the new node and the selected node if the random number is less than `p_e`
        if random.random() < p_e:
            g.add_edge(new_comer, j)
            nds.remove(j) 

    # Handles the positioning of the new node
    g.pos[new_comer] = (0,0)

    # Handles the positioning of the nodes
    g.pos = nx.spring_layout(g, pos = g.pos, iterations = 3)

def pref_select(nds):
    global g
    r = uniform(0, sum([g.degree(i) for i in nds]))
    x = 0

    for i in nds:
        x += g.degree(i)
        if r <= x:
            return i

def get_average_degree_per_node():
    '''
    Calculates the average degrees of the nodes in the graph.

    Returns:
        float: The average degree of the nodes in the graph rounded to 3 decimal places.
    '''
    global g
    degree_sum = sum([g.degree(node) for node in g.nodes])
    return round(float(degree_sum) / len(g.nodes), 3)

    
number_of_simulations = 100 # number of simulations to run
iterations_per_graph = 1000
degree_avgs = []

for i in range(number_of_simulations):
    print(f"Simulation {i+1} of {number_of_simulations}")
    initialize() # Reset the graph to the initial state
    for _ in range(iterations_per_graph):
        update()
    degree_avgs.append(get_average_degree_per_node())

plot_average_degrees(degree_avgs)

# Print the average and standard deviation of the degree distribution
print(f"Average degree: {np.mean(degree_avgs)}")
print(f"Standard deviation of degree distribution: {np.std(degree_avgs)}")
