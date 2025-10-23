def bubble_sort(arr):
    n = len(arr) - 1
    for i in range(n):
        for j in range(n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


my_list = [64, 34, 25, 12, 22, 11, 90]
# my_list = input().split()
# my_list = list(map(int, my_list))
bubble_sort(my_list)
print("Отсортированный список:", my_list)