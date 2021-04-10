import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(3,5)
G.add_edge(3,7)
G.add_edge(3,8)
G.add_edge(3,10)
G.add_edge(4,5)
G.add_edge(4,7)
G.add_edge(5,7)
G.add_edge(6,7)
G.add_edge(8,9)
G.add_edge(8,10)
G.add_edge(9,10)
G.add_edge(10,11)

options = {
    "font_size": 24,
    "node_size": 1000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 2,
    "width": 5,
}
nx.draw_networkx(G, **options)

print(nx.algorithms.core.k_core(G))

ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
