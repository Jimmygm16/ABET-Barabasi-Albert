from pylab import *
import networkx as nx

m0= 100 # numero de nodos al inicio de la red 
m = 4 # numero de enlaces para cada nuevo nodo 

def initialize(p_s_value):
    global g, p_i, p_r, p_s
    p_i = 0.5  # Probabilidad de infección
    p_r = 0.2  # Probabilidad de recuperación
    p_s = p_s_value  # Probabilidad de corte (variable)
    
    g = nx.barabasi_albert_graph(m0, m)  
    g.pos = nx.spring_layout(g)

    for i in g.nodes:
        g.nodes[i]['state'] = 1 if random() < 0.5 else 0  # Estado inicial aleatorio

def observe(step, p_s_value):
    global g, infected_counts
    #cla()
    #title(f"Step: {step} | p_s: {p_s_value:.2f}")
    #nx.draw(g, 
    #        cmap=cm.Wistia, 
    #        vmin=0, vmax=1, 
    #        node_color=[g.nodes[i]['state'] for i in g.nodes], 
    #        pos=g.pos, 
    #        node_size=50)
    infected = sum([g.nodes[i]['state'] for i in g.nodes])
    infected_counts.append(infected)

def update():
    global g, p_i, p_r, p_s
    a = choice(list(g.nodes))
    
    if g.nodes[a]['state'] == 0:
        if g.degree(a) > 0:
            b = choice(list(g.neighbors(a)))
            if g.nodes[b]['state'] == 1:
                if random() < p_s:
                    g.remove_edge(a, b)
                else:
                    if random() < p_i:
                        g.nodes[a]['state'] = 1
    else:
        if random() < p_r:
            g.nodes[a]['state'] = 0

# distintas probabilidades de corte
p_s_values = linspace(0.0, 1.0, 9) 
results = []

fig, axes = subplots(3, 3, figsize=(12, 10))
fig.suptitle("Evolución de Infectados para Diferentes Valores de $p_s$", fontsize=16)

for index, p_s_value in enumerate(p_s_values):
    infected_counts = []
    initialize(p_s_value)
    for step in range(500):
        observe(step, p_s_value)
        pause(0.05)
        update()
    print('p_s values: ', p_s_value)
    results = infected_counts.copy()
    print(results)
    # Ubicar el subplot correcto
    row = index // 3
    col = index % 3
    ax = axes[row, col]

    ax.plot(range(len(infected_counts)), infected_counts, marker='o', markersize=2)
    ax.set_title(f"p_s = {p_s_value:.2f}")
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Infectados")
    ax.grid(True)

# Ajuste del diseño para evitar solapamientos
tight_layout(rect=[0, 0, 1, 0.95])

# Mostrar todas las gráficas en una sola figura
show()