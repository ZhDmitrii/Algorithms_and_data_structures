def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_value = arr[i]
        min_index = i

        for j in range(i + 1, n):
            if min_value > arr[j]:
                min_value = arr[j]
                min_index = j

        if min_index != i:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp


my_list = [64, 34, 25, 12, 22, 11, 90]
# my_list = input().split(",")
# my_list = list(map(int, my_list))
selection_sort(my_list)
print("Отсортированный список:", my_list)
