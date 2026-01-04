import matplotlib.pyplot as plt
import numpy as np


def draw_branch(x, y, angle, length, depth):
    """Рекурсивна функція для малювання дерева Піфагора"""
    if depth == 0:
        return
    
    # Обчислюємо кінцеву точку гілки
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)
    
    # Малюємо гілку
    plt.plot([x, x_end], [y, y_end], 'brown', linewidth=depth*0.5)
    
    # Обчислюємо нову довжину (по теоремі Піфагора)
    new_length = length * 0.7
    
    # Ліва гілка (під кутом +45 градусів)
    draw_branch(x_end, y_end, angle + np.pi/4, new_length, depth - 1)
    
    # Права гілка (під кутом -45 градусів)
    draw_branch(x_end, y_end, angle - np.pi/4, new_length, depth - 1)

# Налаштування вікна для малювання
plt.figure(figsize=(10, 10))
plt.axis('off')
plt.axis('equal')

# Запитуємо глибину у користувача
depth = int(input("Введіть рівень рекурсії (рекомендовано 8-12): "))

# Початкові параметри
start_x = 0
start_y = 0
start_angle = np.pi / 2  # 90 градусів (вгору)
start_length = 3

# Малюємо дерево
draw_branch(start_x, start_y, start_angle, start_length, depth)

plt.title(f"Дерево Піфагора (рівень рекурсії: {depth})", fontsize=14)
plt.show()