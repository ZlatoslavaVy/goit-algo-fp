items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    """
    Жадібний алгоритм для вибору страв з максимальним співвідношенням калорій до вартості.
    """
    total_calories = 0
    remaining_budget = budget
    chosen_items = []
    
    # Створюємо список страв з співвідношенням калорій до вартості
    sorted_items = []
    for item, details in items.items():
        ratio = details["calories"] / details["cost"]
        sorted_items.append((item, details, ratio))
    
    # Сортуємо за співвідношенням від найбільшого до найменшого
    sorted_items.sort(key=lambda x: x[2], reverse=True)
    
    # Обираємо страви поки вистачає бюджету
    for item, details, ratio in sorted_items:
        if details["cost"] <= remaining_budget:
            chosen_items.append(item)
            total_calories += details["calories"]
            remaining_budget -= details["cost"]
    
    return total_calories, budget - remaining_budget, chosen_items


def dynamic_programming(items, budget):
    """
    Алгоритм динамічного програмування для знаходження оптимального набору страв.
    """
    item_names = list(items.keys())
    
    # Створюємо таблицю DP де рядки - до i-ої страви, стовпці - бюджет
    dp_table = [[0 for x in range(budget + 1)] for y in range(len(items) + 1)]
    
    # Заповнюємо таблицю оптимальних калорій для всіх бюджетів
    for i in range(1, len(items) + 1):
        item_name = item_names[i - 1]
        cost = items[item_name]["cost"]
        calories = items[item_name]["calories"]
        
        for j in range(budget + 1):
            # Якщо страва не вміщується в поточний бюджет
            if cost > j:
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                # Вибираємо максимум: взяти страву чи ні
                dp_table[i][j] = max(
                    dp_table[i - 1][j],
                    dp_table[i - 1][j - cost] + calories
                )
    
    # Відновлюємо набір вибраних страв через таблицю
    chosen_items = []
    temp_budget = budget
    
    for i in range(len(items), 0, -1):
        # Якщо значення змінилося - страву було взято
        if dp_table[i][temp_budget] != dp_table[i - 1][temp_budget]:
            item_name = item_names[i - 1]
            chosen_items.append(item_name)
            temp_budget -= items[item_name]["cost"]
    
    return dp_table[len(items)][budget], budget - temp_budget, chosen_items


# Тестування функцій
if __name__ == "__main__":
    budget = 100
    
    # Виконуємо обидва алгоритми
    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)
    
    print(f"Бюджет: {budget} грн\n")
    
    print("Жадібний алгоритм:")
    print(f"Калорії: {greedy_result[0]}, Витрачено: {greedy_result[1]} грн")
    print(f"Вибрані страви: {greedy_result[2]}\n")
    
    print("Динамічне програмування:")
    print(f"Калорії: {dp_result[0]}, Витрачено: {dp_result[1]} грн")
    print(f"Вибрані страви: {dp_result[2]}")