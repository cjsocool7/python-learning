# Python Learning

## Day 1 - Python Classes

### What I learned
- What a class is and why it exists
- The difference between a class and an instance
- Created `person` class from scratch as an exercise

## Day 2 - Dataclasses, UUID and Nodes
- What `dataclass` are and why they are cleaner than regular classes
- What `UUID` is and why we use it for IDs instead of regular numbers
- Built day2_node.py to add to my mind map app

## Day 3 - Edges
- What an `Edge` represents conceptually; a relationship between two IDs
- Create `Node` and an `Edge` that references it, then print everything out

## Day 4 — Graph Model & Dictionaries

- Learned the difference between lists and dictionaries
- Learned when to use each data structure
- Built the `Graph` model as a container for all nodes and edges
- Used `field(default_factory=dict)` to give each Graph its own dictionary
- Connected `Node` and `Edge` models through the Graph
- Learned the difference between functions and methods

# Day 5 - CLI Testing with sys.argv

- Learned what `sys.argv` is and how it captures terminal input as a list
- Learned `if __name__ == "__main__"` and why it prevents code from running on import
- Built a CLI script that reads commands from the terminal
- Implemented `add-node` and `list-nodes` commands using the Graph model
- Fixed import paths to use full folder references (`from models.node import Node`)
- `sys.argv`         → everything you typed in terminal as a list
- `sys.argv[0]`      → filename
- `sys.argv[1]`     → your command
- `sys.argv[2]`      → your first argument
- `if __name__`      → only run when file is run directly