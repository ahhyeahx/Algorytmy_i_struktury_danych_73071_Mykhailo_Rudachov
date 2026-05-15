import networkx as nx
import matplotlib.pyplot as plt

# a)
G = nx.Graph()
wierzcholki = ['A', 'B', 'C', 'D', 'E', 'F']
G.add_nodes_from(wierzcholki)

krawedzie = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F'), ('B', 'E')]
G.add_edges_from(krawedzie)

# b i c)
plt.figure(figsize=(6, 4))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray',
        node_size=1500, font_size=12, font_weight='bold')

plt.title("Przykładowy Graf Nieskierowany")
plt.show()