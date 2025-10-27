def quick_sort(arr):
    if len(arr) <= 1:
        return arr # Если массив пустой или содержит один элемент, он считается отсортированным.

    pivot = arr[len(arr) // 2] # Выбираем опорный элемент (в данном случае средний элемент).
    left = [x for x in arr if x < pivot] # Элемент меньше опорного.
    middle = [x for x in arr if x == pivot] # Элементы равные опорному.
    right = [x for x in arr if x > pivot] # Элементы больше опорного.

    # Рекурсивно сортируем левую и правую части, а затем объединяем их с опорным элементом
    return quick_sort(left) + middle + quick_sort(right)

# Пример использования:
#my_list = [64, 34, 25, 12, 22, 11, 90]
my_list = input().split(",")
my_list = list(map(int, my_list))
sorted_list = quick_sort(my_list)
print("Отсортированный список:", sorted_list)