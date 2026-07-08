from dataclasses import dataclass
from uuid import uuid4
from day2_node import Node

@dataclass
class Edge:
    id:str
    source_id:str
    target_id:str

node1=Node(
    id=str(uuid4()),
    label="Hello",
    x=0.0,
    y=0.0
)

node2=Node(
    id=str(uuid4()),
    label="World",
    x=5.0,
    y=0.0
)
edge1=Edge(
    id=str(uuid4()),
    source_id=node1.id,
    target_id=node2.id
)

print(f"source: {node1.id}")
print(f"target: {node2.id}")
print(f"source: {edge1.source_id}, target: {edge1.target_id}")