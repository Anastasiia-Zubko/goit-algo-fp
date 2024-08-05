import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Node color
        self.id = str(uuid.uuid4())  # Unique identifier for each node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Use id and store node value
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, highlight_nodes=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Use node value for labels

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    
    if highlight_nodes:
        highlight_colors = [highlight_nodes.get(node, "#000000") for node in tree.nodes()]
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=highlight_colors)

    plt.show()

def build_heap_tree(heap):
    nodes = [Node(val) for val in heap]
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
    return nodes[0] if nodes else None

def color_gradient(n):
    return [f"#{i * 255 // (n - 1):02x}00ff" for i in range(n)]


def dfs_iterative(tree_root):
    stack = [tree_root]
    visited = set()
    order = {}
    color_steps = color_gradient(len(list(iterate_nodes(tree_root))))
    step = 0

    while stack:
        node = stack.pop()
        if node and node not in visited:
            visited.add(node)
            order[node.id] = color_steps[step]
            step += 1
            stack.extend([node.right, node.left])
    draw_tree(tree_root, order)

def bfs_iterative(tree_root):
    queue = deque([tree_root])
    visited = set()
    order = {}
    color_steps = color_gradient(len(list(iterate_nodes(tree_root))))
    step = 0

    while queue:
        node = queue.popleft()
        if node and node not in visited:
            visited.add(node)
            order[node.id] = color_steps[step]
            step += 1
            queue.extend([node.left, node.right])
    draw_tree(tree_root, order)

def iterate_nodes(node):
    if node:
        yield node
        yield from iterate_nodes(node.left)
        yield from iterate_nodes(node.right)

def main():
    # Example heap
    heap = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # Build binary heap tree
    heap_root = build_heap_tree(heap)

    print("Visualizing DFS traversal:")
    dfs_iterative(heap_root)

    print("Visualizing BFS traversal:")
    bfs_iterative(heap_root)

if __name__ == "__main__":
    main()
