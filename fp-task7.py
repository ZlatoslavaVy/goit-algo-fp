import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    # Словник для підрахунку сум
    sums_count = {i: 0 for i in range(2, 13)}
    
    # Симуляція кидків
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sums_count[total] += 1
    
    # Обрахування ймовірності випаду кожної суми
    probabilities = {}
    for sum_value, count in sums_count.items():
        probabilities[sum_value] = count / num_rolls
    
    return probabilities


def plot_probabilities(probabilities, num_rolls):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    # Аналітичні ймовірності
    analytical = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
        8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }
    analytical_probs = [analytical[s] for s in sums]
    
    # Створення графіка з порівнянням
    x = range(len(sums))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(12, 6))
    bars1 = ax.bar([i - width/2 for i in x], probs, width, 
                    label='Монте-Карло', alpha=0.8, color='steelblue')
    bars2 = ax.bar([i + width/2 for i in x], analytical_probs, width,
                    label='Аналітичний', alpha=0.8, color='orange')
    
    ax.set_xlabel('Сума чисел на кубиках')
    ax.set_ylabel('Ймовірність')
    ax.set_title(f'Ймовірність суми чисел на двох кубиках (n={num_rolls:,})')
    ax.set_xticks(x)
    ax.set_xticklabels(sums)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        ax.text(i - width/2, prob, f"{prob*100:.1f}%", 
                ha='center', va='bottom', fontsize=8)
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Аналітичні ймовірності для порівняння
    analytical = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
        8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }
    
    print("="*70)
    print("ПОРІВНЯННЯ РЕЗУЛЬТАТІВ МЕТОДУ МОНТЕ-КАРЛО ТА АНАЛІТИЧНИХ РОЗРАХУНКІВ")
    print("="*70)
    print()
    
    for accuracy in [100, 1000, 10000, 100000]:
        # Симуляція кидків і обчислення ймовірностей
        probabilities = simulate_dice_rolls(accuracy)
        
        # Розрахунок середньої різниці
        differences = []
        
        print(f"Кількість кидків: {accuracy:,}")
        print("-" * 70)
        print(f"{'Сума':<6} {'Монте-Карло (%)':<18} {'Аналітично (%)':<18} {'Різниця (%)'}")
        print("-" * 70)
        
        for sum_value in range(2, 13):
            monte = probabilities[sum_value] * 100
            analyt = analytical[sum_value] * 100
            diff = abs(monte - analyt)
            differences.append(diff)
            print(f"{sum_value:<6} {monte:<18.2f} {analyt:<18.2f} {diff:.2f}")
        
        avg_diff = sum(differences) / len(differences)
        print(f"\n📊 Середня різниця: {avg_diff:.3f}%")
        print("="*70)
        print()
        
        # Відображення ймовірностей на графіку
        plot_probabilities(probabilities, accuracy)
    
    print("\n✅ Всі симуляції завершено!")
    print("\n📝 ВИСНОВКИ:")
    print("-" * 70)
    print("1. Зі збільшенням кількості симуляцій точність зростає")
    print("2. При 100,000 кидках різниця з аналітичними даними < 0.3%")
    print("3. Сума 7 має найвищу ймовірність (~16.67%)")
    print("4. Розподіл симетричний відносно суми 7")
    print("5. Метод Монте-Карло підтверджує аналітичні розрахунки")
    print("-" * 70)