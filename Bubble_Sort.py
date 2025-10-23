def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# my_list = [64, 34, 25, 12, 22, 11, 90]
my_list = input().split(",")
my_list = list(map(int, my_list))
bubble_sort(my_list)
print("Отсортированный список:", my_list)