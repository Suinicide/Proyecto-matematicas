import networkx as nx
import urllib.request
import matplotlib.pyplot as plt
plt.switch_backend('tkagg')
import time
import pandas as pd
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# ============================
# DESCARGAR Y CARGAR EL GRAFO
# ============================

url = "https://snap.stanford.edu/data/email-Eu-core.txt.gz"
local_path = "email-Eu-core.txt.gz"
urllib.request.urlretrieve(url, local_path)

G = nx.read_edgelist(local_path, create_using=nx.Graph(), nodetype=int)

print(f"Número de nodos: {G.number_of_nodes()}")
print(f"Número de aristas: {G.number_of_edges()}")

# ============================
# HISTOGRAMA DE GRADOS
# ============================

degrees = [deg for _, deg in G.degree()]
plt.hist(degrees, bins=30, color='skyblue', edgecolor='black')
plt.title("Distribución de grados")
plt.xlabel("Grado")
plt.ylabel("Número de nodos")
plt.grid(True)
plt.show()

# ============================
# CENTRALIDAD POR GRADO
# ============================

degree_centrality = nx.degree_centrality(G)
top_5 = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nTop 5 nodos más centrales (por grado):")
for node, centrality in top_5:
    print(f"Nodo {node} - Centralidad: {centrality:.4f}")

# ============================
# FILTRACIÓN PARA QUITAR DENSIDAD
# ============================

DEGREE_MIN = 20   # <-- puedes subirlo si quieres un grafo aún más limpio

filtered_nodes = [n for n, d in G.degree() if d >= DEGREE_MIN]
G_filtered = G.subgraph(filtered_nodes).copy()

print(f"\nNodos después de filtrar: {G_filtered.number_of_nodes()}")
print(f"Aristas después de filtrar: {G_filtered.number_of_edges()}")

# ============================
# VISUALIZACIÓN DEL GRAFO FILTRADO
# ============================

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G_filtered, seed=42)

nx.draw(
    G_filtered,
    pos,
    node_size=20,
    edge_color='gray',
    with_labels=False
)

plt.title(f"Visualización del grafo filtrado (grado ≥ {DEGREE_MIN})")
plt.show()
