import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Генерируем список из 10 случайных чисел от 1 до 100
my_list = [random.randint(1, 100) for _ in range(10)]
print("Исходный список:", my_list)

sorted_list = bubble_sort(my_list)
print("Отсортированный список:", sorted_list)