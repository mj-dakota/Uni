import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Parte A
print("Parte A: Matriz de adyacencia y matriz de caminos")

A = np.array([
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 1, 0]
])

print("Matriz de Adyacencia A:")
print(A)

# Matriz de caminos P
def warshall(matrix):
    n = len(matrix)
    reach = matrix.copy()
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    return reach

P = warshall(A.copy())
print("\nMatriz de caminos P (con Warshall):")
print(P)

# Parte B
print("\nParte B: Caminos de longitud k de v1 a v4")

def caminos_longitud_k(A, k, origen, destino):
    Ak = np.linalg.matrix_power(A, k)
    return Ak[origen][destino]

for k in range(1, 5):
    print(f"Número de caminos de longitud {k} de v1 a v4:", caminos_longitud_k(A, k, 0, 3))

print("\nVerificación de conectividad")

def verificar_conectividad(P):
    if np.all(P):
        return "El grafo es fuertemente conexo"
    elif np.any(P):
        return "El grafo es unilateralmente conexo"
    else:
        return "El grafo es débilmente conexo"

resultado = verificar_conectividad(P)
print(resultado)

# Parte C
G = nx.DiGraph(A)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', arrows=True)
plt.title("Grafo 9.26")
plt.show()
