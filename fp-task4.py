import uuid
import heapq

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_heap_tree(heap, index=0):
    """Реалізація функції побудови дерева бінарної купи"""
    # Перевіряємо, чи індекс не виходить за межі масиву
    if index >= len(heap):
        return None
    
    # Створюємо новий вузол з поточним значенням
    node = Node(heap[index])
    
    # Обчислюємо індекси дочірніх вузлів за формулами купи
    left = index * 2 + 1   # Лівий нащадок
    right = index * 2 + 2  # Правий нащадок
    
    # Рекурсивно будуємо ліве і праве піддерева
    node.left = build_heap_tree(heap, left)
    node.right = build_heap_tree(heap, right)
    
    return node


def visualize_heap(heap):
    """Функція для візуалізації бінарної купи"""
    # Перевіряємо, чи купа не порожня
    if not heap:
        print("Купа порожня!")
        return
    
    # Будуємо дерево з масиву купи
    heap_root = build_heap_tree(heap)
    
    # Візуалізуємо побудоване дерево
    draw_tree(heap_root)


if __name__ == '__main__':
    # Припустимо, що у нас є бінарна купа у вигляді списку
    heap_list = [1, 3, 5, 7, 9, 2]
    heapq.heapify(heap_list)
    print(heap_list)
    # Побудова дерева з купи
    heap_tree_root = build_heap_tree(heap_list)


    # Візуалізація дерева бінарної купи
    draw_tree(heap_tree_root)