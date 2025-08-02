import json
import networkx as nx

data = json.load(open('network_graph.json'))

graph = nx.Graph()
graph.add_weighted_edges_from(
    (edge["source"], edge["target"], edge["weight"])
    for edge in data["edges"]
)

#print(graph)
print(nx.shortest_path(graph, 'user_103', 'user_589', weight = 'weight'))