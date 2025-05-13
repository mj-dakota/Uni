import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

A = np.array([
    [0, 2, 0, 1],
    [0, 0, 1, 1],
    [2, 1, 0, 0],
    [0, 0, 1, 1]
])

G = nx.MultiDiGraph()

n = A.shape[0]
G.add_nodes_from(range(1, n+1))

for i in range(n):
    for j in range(n):
        for _ in range(A[i][j]):
            G.add_edge(i+1, j+1)

pos = nx.circular_layout(G)
plt.figure(figsize=(8,6))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=15, arrows=True)
plt.title("Problema 9.15 - Multigrafo dirigido")
plt.show()
