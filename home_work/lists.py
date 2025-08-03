''' Принцип роботи алгоритму
1. Поміщаємо в мін-купу перший елемент кожного списку разом з інформацією про те, з якого він списку та його індекс.
2. Дістаємо найменший елемент із купи, додаємо його у результат.
3. Якщо у цьому ж списку є наступний елемент — додаємо його у купу.
4. Повторюємо, поки купа не порожня.

Часова складність: O(N log k), де
N — загальна кількість елементів,
k — кількість списків.'''

import heapq

def merge_k_lists(lists):
    min_heap = []
    
    # 1ніціалізація купи першим елементом кожного списку
    for list_idx, lst in enumerate(lists):
        if lst:  # перевірка, що список не порожній
            heapq.heappush(min_heap, (lst[0], list_idx, 0))
    
    merged_list = []
    
    # Витягуємо елементи з купи та додаємо наступні
    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(value)
        
        # Якщо в списку ще є елементи, додаємо наступний у купу
        if element_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, element_idx + 1))
    
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
