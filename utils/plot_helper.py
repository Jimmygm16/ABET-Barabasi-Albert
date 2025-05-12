import matplotlib.pyplot as plt

def plot_average_degrees(degree_avgs: dict):
    """
    Plots the average degree of nodes in a Barabasi-Albert graph.

    Parameters:
    degree_avgs (list): A list of average degrees for each iteration.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(degree_avgs, label='Average Degree')
    plt.title('Average Degree of Nodes in Barabasi-Albert Graph')
    plt.xlabel('Iteration')
    plt.ylabel('Average Degree')
    plt.legend()
    plt.grid()
    plt.savefig("plots/average_degree_plot.png")

def plot_edge_avg_over_time(edge_avg: list):
    """
    Plots the average degree of nodes in a Barabasi-Albert graph.

    Parameters:
        edge_avg (list): A list of average degrees for each iteration.
    """	
    plt.figure(figsize=(10, 6))
    plt.plot(edge_avg, label='Edge Average')
    plt.title('Edge Average Over Time')
    plt.xlabel('Iteration')
    plt.ylabel('Edge Average')
    plt.legend()
    plt.grid()
    plt.savefig("edge_avg_over_time.png")