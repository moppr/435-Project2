import random
from node import Node

if __name__ == "__main__":
    n = Node(5)
    n2 = Node(5)
    print(hash(n))
    print(hash(n2))
    n.edges.add(6)
    print(n.edges)
    print(n2.edges)
