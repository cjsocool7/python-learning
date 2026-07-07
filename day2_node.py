from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Node:
    id: str
    label: str
    x: float
    y: float

node1 = Node(
    id=str(uuid4()),
    label="topic",
    x=0.0,
    y=0.0
)

print(node1)
print(node1.id)