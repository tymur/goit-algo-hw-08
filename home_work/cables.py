import heapq

def min_connection_cost(cables):
    # Створюємо мін-купу з довжин кабелів
    heapq.heapify(cables)
    total_cost = 0

    # Повторюємо, поки не залишиться один кабель
    while len(cables) > 1:
        # Дістаємо два найкоротших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Витрати на їх об’єднання
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальні загальні витрати:", min_connection_cost(cables))

# Очікуваний результат для цього конкретного прикладу: 29