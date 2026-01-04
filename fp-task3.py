import heapq

import networkx as nx
import matplotlib.pyplot as plt


# Створення власного вагового графа (складний для перевірки роботи алгоритму)
G = nx.Graph()

# Додаємо ребра з вагами для складнішого графа
G.add_edge("A", "B", weight=4)
G.add_edge("A", "C", weight=2)
G.add_edge("B", "C", weight=1)
G.add_edge("B", "D", weight=5)
G.add_edge("C", "D", weight=8)
G.add_edge("C", "E", weight=10)
G.add_edge("D", "E", weight=2)
G.add_edge("D", "F", weight=6)
G.add_edge("E", "F", weight=3)

print("Граф створено з вершинами:", list(G.nodes()))
print("Кількість ребер:", G.number_of_edges())
print()


# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    """
    Алгоритм Дейкстри з використанням бінарної купи (heapq)
    
    Args:
        graph: NetworkX граф
        start: початкова вершина
    
    Returns:
        shortest_paths: словник найкоротших відстаней
        previous: словник попередніх вершин для відновлення шляху
    """
    # Ініціалізація відстаней
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    
    # Словник для відстеження попередніх вершин
    previous = {vertex: None for vertex in graph}
    
    # Бінарна купа (priority queue) - ключова структура для оптимізації!
    # Формат: (відстань, вершина)
    priority_queue = [(0, start)]
    
    # Множина відвіданих вершин
    visited = set()
    
    # Основний цикл алгоритму Дейкстри
    while priority_queue:
        # Витягуємо вершину з мінімальною відстанню (використовуємо купу!)
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Якщо вершина вже оброблена, пропускаємо
        if current_vertex in visited:
            continue
        
        # Позначаємо вершину як відвідану
        visited.add(current_vertex)
        
        # Перевіряємо всіх сусідів поточної вершини
        for neighbor in graph.neighbors(current_vertex):
            # Отримуємо вагу ребра
            edge_weight = graph[current_vertex][neighbor]['weight']
            
            # Обчислюємо нову відстань до сусіда
            distance = current_distance + edge_weight
            
            # Якщо знайшли коротший шлях до сусіда
            if distance < shortest_paths[neighbor]:
                # Оновлюємо найкоротшу відстань
                shortest_paths[neighbor] = distance
                # Запам'ятовуємо попередню вершину для побудови шляху
                previous[neighbor] = current_vertex
                # Додаємо сусіда до купи для подальшої обробки
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths, previous


def get_path(previous, start, end):
    """Відновлення шляху від start до end"""
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = previous[current]
    
    path.reverse()
    
    if path[0] == start:
        return path
    else:
        return []


# Використання алгоритму Дейкстри
start_vertex = "A"
shortest_paths, previous = dijkstra(G, start_vertex)

print(f"Найкоротші відстані від вершини '{start_vertex}':")
print("-" * 50)
for vertex in sorted(shortest_paths.keys()):
    distance = shortest_paths[vertex]
    if distance != float('infinity'):
        path = get_path(previous, start_vertex, vertex)
        path_str = " -> ".join(path)
        print(f"{start_vertex} -> {vertex}: відстань = {distance}, шлях: {path_str}")
print()


# Візуалізація графа
plt.figure(figsize=(12, 8))

pos = nx.spring_layout(G, seed=42)  # Positions for all nodes

# Малюємо вершини (початкова - зеленим, інші - блакитним)
node_colors = ['lightgreen' if node == start_vertex else 'lightblue' 
               for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=700, node_color=node_colors)

# Малюємо всі ребра сірим
nx.draw_networkx_edges(G, pos, width=2, alpha=0.3, edge_color='gray')

# Виділяємо найкоротші шляхи червоним
shortest_path_edges = []
for vertex in previous:
    if previous[vertex] is not None:
        # Додаємо обидва напрямки для недирективного графа
        shortest_path_edges.append((previous[vertex], vertex))

nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, 
                       width=4, edge_color='red')

# Підписи ваг ребер
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

# Підписи вершин
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif", 
                        font_weight='bold')

# Додаємо легенду
legend_text = f"Алгоритм Дейкстри\n"
legend_text += f"Початкова вершина: {start_vertex}\n\n"
legend_text += "Відстані:\n"
for vertex in sorted(shortest_paths.keys()):
    if shortest_paths[vertex] != float('infinity'):
        legend_text += f"{vertex}: {shortest_paths[vertex]}\n"

plt.text(0.02, 0.98, legend_text, transform=plt.gca().transAxes,
        fontsize=11, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.title("Алгоритм Дейкстри з використанням бінарної купи (heapq)", 
         fontsize=14, fontweight='bold')
plt.axis("off")
plt.tight_layout()
plt.show()

print("Візуалізація завершена!")
print("Червоні ребра - найкоротші шляхи від вершини", start_vertex)