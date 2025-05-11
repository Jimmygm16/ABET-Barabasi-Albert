from pylab import *
import networkx as nx
import random
from plot_helper import plot_average_degrees

m0= 100 # numero de nodos al inicio de la red 
m = 4 # numero de enlaces para cada nuevo nodo 

def initialize():
    global g
    g = nx.barabasi_albert_graph(m0, m)
    g.pos = nx.spring_layout(g)
    g.count = 0 

def observe():
    global g
    cla()
    nx.draw(g, pos = g.pos, cmap= cm.bwr , vmin=0, vmax=1)

def update():
    global g
    g.count +=1
    if g.count % 20 == 0:
        p_e = random.random()
        nds = list(g.nodes)
        new_comer = max(nds) + 1
        for i in range(m):
            j = pref_select(nds)
            g.add_edge(new_comer, j) if random() < p_e else None
            nds.remove(j)
        g.pos[new_comer] = (0,0)
    
    g.pos = nx.spring_layout(g, pos = g.pos, iterations = 3)

def get_average_degree_per_node():
    '''
    Calculates the average degrees of the nodes in the graph.
    '''
    global g
    degree_sum = sum([g.degree(node) for node in g.nodes])
    return degree_sum / len(g.nodes)

def pref_select(nds):
    global g
    r = uniform(0, sum([g.degree(i) for i in nds]))
    x = 0

    for i in nds:
        x += g.degree(i)
        if r <= x:
            return i
        
degree_avgs = []
for i in range(10):
    initialize()
    for _ in range(10):
        observe()
        pause(0.05)
        update()
    degree_avgs.append(get_average_degree_per_node())
    print(degree_avgs)
plot_average_degrees(degree_avgs)
