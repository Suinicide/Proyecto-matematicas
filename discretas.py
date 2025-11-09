import networkx as nx
import urllib.request
import matplotlib.pyplot as plt
import time
import pandas as pd
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

url = "https://snap.stanford.edu/data/email-Eu-core.txt.gz"
local_path = "email-Eu-core.txt.gz"
urllib.request.urlretrieve(url, local_path)
G = nx.read_edgelist(local_path, create_using=nx.Graph(), nodetype=int)

print(f"Número de nodos: {G.number_of_nodes()}")
print(f"Número de aristas: {G.number_of_edges()}")

degrees = [deg for _, deg in G.degree()]
plt.hist(degrees, bins=30, color='skyblue', edgecolor='black')
plt.title("Distribución de grados")
plt.xlabel("Grado")
plt.ylabel("Número de nodos")
plt.grid(True)
plt.show()

degree_centrality = nx.degree_centrality(G)
top_5 = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nTop 5 nodos más centrales (por grado):")
for node, centrality in top_5:
    print(f"Nodo {node} - Centralidad: {centrality:.4f}")

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, node_size=20, edge_color='gray', with_labels=False)
plt.title("Visualización del grafo (layout de fuerza)")
plt.show()


rsa_keys = {}
for node, _ in top_5:
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    rsa_keys[node] = {
        "private": private_key,
        "public": public_key
    }

print("\n Claves RSA generadas para los 5 nodos más centrales.")

mensaje = b"Este es un mensaje confidencial entre nodos centrales."
resultados = []

for node, keys in rsa_keys.items():
    public_key = keys["public"]
    private_key = keys["private"]

    t1 = time.perf_counter()
    mensaje_cifrado = public_key.encrypt(
        mensaje,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    t2 = time.perf_counter()

    t3 = time.perf_counter()
    mensaje_descifrado = private_key.decrypt(
        mensaje_cifrado,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    t4 = time.perf_counter()

    resultados.append({
        "nodo": node,
        "tiempo_cifrado_ms": (t2 - t1) * 1000,
        "tiempo_descifrado_ms": (t4 - t3) * 1000,
        "tamano_cifrado_bytes": len(mensaje_cifrado),
        "verificacion_correcta": mensaje_descifrado == mensaje
    })

df_resultados = pd.DataFrame(resultados)
print("\n📋 Tabla de resultados:")
print(df_resultados)

df_resultados.to_csv("resultados_rsa.csv", index=False)
print("\nArchivo CSV exportado como 'resultados_rsa.csv'")

plt.figure(figsize=(8, 5))
plt.bar(df_resultados['nodo'], df_resultados['tiempo_cifrado_ms'], label='Cifrado', color='steelblue')
plt.bar(df_resultados['nodo'], df_resultados['tiempo_descifrado_ms'], label='Descifrado', color='orange', alpha=0.7)
plt.xlabel("Nodo")
plt.ylabel("Tiempo (ms)")
plt.title("Tiempos de cifrado y descifrado por nodo")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(df_resultados['nodo'], df_resultados['tamano_cifrado_bytes'], color='green')
plt.xlabel("Nodo")
plt.ylabel("Tamaño del mensaje cifrado (bytes)")
plt.title("Tamaño del mensaje cifrado por nodo")
plt.grid(True)
plt.show()
