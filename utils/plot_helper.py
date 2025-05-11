import matplotlib.pyplot as plt

def plot_average_degrees(degree_avgs):
    """
    Plots the average degree of nodes in a Barabasi-Albert graph.

    Parameters:
    degree_avgs (list): A list of average degrees to plot.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(degree_avgs, marker='o', linestyle='-', color='b')
    plt.title('Average Degree of Nodes in Barabasi-Albert Graph')
    plt.xlabel('Iteration')
    plt.ylabel('Average Degree')
    plt.grid()
    plt.show()
