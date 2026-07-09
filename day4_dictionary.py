from dataclasses import dataclass, field
from uuid import uuid4
from day2_node import Node
from day3_edge import Edge

@dataclass
class Graph:
    nodes: dict = field(default_factory=dict)
    edges: dict = field(default_factory=dict)

    def add_node(self, node):
        self.nodes[node.id] = node

    def add_edge(self, edge):
        self.edges[edge.id] = edge

    def get_all_nodes(self):
        return self.nodes
    
    def get_all_edges(self):
        return self.edges
    
# create a graph
graph = Graph()

# create two nodes
node1 = Node(
    id=str(uuid4()),
    label="Main Idea",
    x=400.0,
    y=300.0
)

node2 = Node(
    id=str(uuid4()),
    label="Sub Idea",
    x=600.0,
    y=200.0
)

# create an edge connecting them
edge1 = Edge(
    id=str(uuid4()),
    source_id=node1.id,
    target_id=node2.id
)

# add everything to the graph
graph.add_node(node1)
graph.add_node(node2)
graph.add_edge(edge1)

# print everything
print(graph.get_all_nodes())
print(graph.get_all_edges())

